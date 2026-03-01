import json
from urllib.parse import parse_qs

from django.core import serializers
from django.db.models import F, Q, OuterRef, QuerySet, Subquery

from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async

from asgiref.sync import sync_to_async

from chat.models import ChatRoom, PrivateRoom, Message, User
from utilities.redis import presence


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        pass


class PresenceConsumer(AsyncWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        self.redis_client = presence.RedisClient(
            host_name="127.0.0.1",
            port=6379,
            db_number=0
        )

        super().__init__(*args, **kwargs)

    async def connect(self):
        self.user: User = self.scope["user"]

        if self.user.is_anonymous:
            await self.close()
            return
        
        await self.accept()

        first_connection: bool = self.redis_client.connect(self.user.username)

        if first_connection:
            await self.channel_layer.group_add(
                f"user_{self.user.username}",
                self.channel_name
            )

            await self.send_group_message("friend_online")

    async def disconnect(self, code):
        last_connection: bool = self.redis_client.disconnect(self.user.username)

        if last_connection:
            # discard the group, if the connection is the last
            await self.channel_layer.group_discard(
                f"user_{self.user.username}",
                self.channel_name
            )

            await self.send_group_message("friend_offline")

    async def send_group_message(self, type):
        friend_ids: list = await self.get_friends()

        for friend_id in friend_ids:
            await self.channel_layer.group_send(
                f"user_{friend_id}",
                {
                    "type": type,
                    "user_id": self.user.username
                }
            )
    
    async def friend_online(self, event: dict) -> None:
        user_id: str = event['user_id']

        await self.indicate_status(user_id, "online")

    async def friend_offline(self, event: dict) -> None:
        user_id: str = event['user_id']

        await self.indicate_status(user_id, "offline")

    async def indicate_status(self, user_id: str, event_type: str) -> None:
        await self.send(
            text_data=json.dumps({
                "type": "indicator",
                "event": event_type,
                "user_id": user_id
            })
        )

    async def receive(self, text_data):
        """
        - find the user in the same room as the one sent
        - send messages to their room
        """
        json_data = json.loads(text_data)

        message_type = json_data['type']

        if message_type == "heartbeat":
            self.redis_client.heartbeat(self.user.username)
            return
        
        room = json_data['room']
        sender = json_data['sender']

        receiver: User = await self.get_receiver(room)
        receivers: list[str] = [self.user.username, receiver.username]

        if message_type == "message":
            message = json_data['message']
            if message is None or message == "":
                return

            await self.save_message(message, room_name=room)

            for receiver in receivers:
                await self.channel_layer.group_send(
                    f"user_{receiver}",
                    {
                        "type": "send_message_to_receiver",
                        "room": room,
                        "message": message,
                        "sender": sender,
                    }
                )
        elif message_type == "typing":
            await self.channel_layer.group_send(
                f"user_{receiver.username}",
                {
                    "type": "send_typing_indicator_to_receiver",
                    "room": room,
                    'sender': sender,
                }
            )

    async def send_typing_indicator_to_receiver(self, event):
        room: str = event['room']
        sender: str = event['sender']

        await self.send(
            text_data=json.dumps({
            'type': "typing",
            'room': room,
            'sender': sender,
        }))

    async def send_message_to_receiver(self, event):
        sender: str = event['sender']
        message: str = event['message']
        room: str = event['room']

        await self.send(
            text_data=json.dumps({
            'type': "chat",
            'message': message,
            'sender': sender,
            'room': room,
        }))

    @database_sync_to_async
    def get_receiver(self, room: str):
        return PrivateRoom.objects.get(
            Q(room__room_name=room) & ~Q(user=self.user)
        ).user
        
    @database_sync_to_async
    def get_friends(self) -> list[str]:
        receiver_subquery = User.objects.filter(
            chatroom=OuterRef('pk')
        ).exclude(id=self.user.id).values('username')[:1]
        
        friends: QuerySet =  self.user.chatroom_set.annotate(
            receiver=Subquery(receiver_subquery),
        ).values_list('receiver', flat=True)

        return [friend for friend in friends]
    
    @database_sync_to_async
    def save_message(self, message, room_name):
        print("-------- SAVE MESSAGE -----------")
        message = Message(
            room=ChatRoom.objects.get(room_name=room_name),
            sender=self.user,
            content=message
        )

        message.save()

        print(Message.objects.last())
        
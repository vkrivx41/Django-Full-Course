from django.core import serializers
from django.db.models import F

from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async

import json
from urllib.parse import parse_qs

from chat.models import ChatRoom, PrivateRoom, Message, User


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        room_name_bytes = self.scope['query_string'].decode()
        query_params = parse_qs(room_name_bytes)

        self.room_name = query_params.get('room')[0]

        await self.channel_layer.group_add(
            self.room_name,
            self.channel_name
        )        

        await self.accept()

        messages = await self.get_group_messages(self.room_name)

        await self.send(
            text_data=json.dumps({
                'type': 'connections.established',
                'messages': messages
            })
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        room_name = text_data_json['room']
        sender = text_data_json['sender']

        if message is None or message == "":
            return
        
        await self.save_message(message, room_name, sender)

        await self.channel_layer.group_send(
            room_name,
            {
                'type': "chat_message",
                'message': message,
                'sender': sender,
            }
        )

    async def chat_message(self, event):
        message = event['message']
        sender = event['sender']

        await self.send(
            text_data=json.dumps({
            'type': "chat",
            'message': message,
            'sender': sender
        }))

    @database_sync_to_async
    def get_group_messages(self, group_name: str):
        room = ChatRoom.objects.get(room_name=group_name)

        messages = Message.objects.filter(
            room=room
        )
        
        return serializers.serialize('json', messages)

    @database_sync_to_async
    def save_message(self, message, room_name, sender):
        message = Message(
            room=ChatRoom.objects.get(room_name=room_name),
            sender=User.objects.get(username=sender),
            content=message
        )

        message.save()
        
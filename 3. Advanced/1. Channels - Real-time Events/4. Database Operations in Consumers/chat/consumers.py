from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async

import json
from urllib.parse import parse_qs

from chat.models import ChatRoom, Message


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        room_name_bytes = self.scope['query_string'].decode()  # decodes the bytes
        query_params = parse_qs(room_name_bytes)  # parse the querystring from key=value to {'key'='value'}

        self.room_group_name = query_params.get('room')[0]  # get the first element
        print(self.room_group_name)

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )        

        await self.accept()

        messages = await self.get_group_messages(self.room_group_name)

        await self.send(
            text_data=json.dumps({
                'type': 'connections.established',
                'room': self.room_group_name,
                'message': 'You are now connected',
                'messages': json.dumps(messages)
            })
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        room_name = text_data_json['room']

        await self.save_message(message, room_name)

        await self.channel_layer.group_send(
            room_name,
            {
                'type': "chat_message",
                'message': message,
                'room': room_name
            }
        )

    async def chat_message(self, event):
        message = event['message']
        room = event['room']

        await self.send(text_data=json.dumps({
            'type': "chat",
            'room': room,
            'message': message,
        }))

    @database_sync_to_async
    def save_message(self, content, room_name):
        room = ChatRoom.objects.get(room_name=room_name)

        message = Message(
            content=content,
            room=room
        )

        message.save()

    @database_sync_to_async
    def get_group_messages(self, room_name) -> dict:
        # we can also use the django.core.serializers serializer method to serializer the queryset
        # serializers.serialize('json', queryset)
        messages = Message.objects.filter(
            room__room_name=room_name
        ).values('content', 'room')

        messages_dict: list = []

        for message in messages:
            msg = {
                'content': message['content'],
                'room': message['room'],
            }
            messages_dict.append(msg)

        return messages_dict
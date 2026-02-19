from channels.generic.websocket import AsyncWebsocketConsumer

import json
import asyncio


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'test'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )        

        await self.accept()

        await self.send(
            text_data=json.dumps({
                'type': 'connections.established',
                'message': 'You are now connected'
            })
        )

    async def receive(self, text_data):
        await asyncio.sleep(5)
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': "chat.message",  # create a function name chat_message to handle this
                'message': message
            }
        )

    async def chat_message(self, event):
        message = event['message']

        print(asyncio.current_task())  # <Task pending name='Task-9' coro=<ASGIStaticFilesHandler.__call__() running

        await self.send(text_data=json.dumps({
            'type': "chat",
            'message': message
        }))

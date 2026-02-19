from channels.generic.websocket import WebsocketConsumer

from asgiref.sync import async_to_sync

import json


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name = 'test'

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )        

        self.accept()

        self.send(
            text_data=json.dumps({
                'type': 'connections.established',
                'message': 'You are now connected'
            })
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': "chat.message",  # create a function name chat_message to handle this
                'message': message
            }
        )

    def chat_message(self, event):
        message = event['message']

        self.send(text_data=json.dumps({
            'type': "chat",
            'message': message
        }))

from django.core import serializers

import json

from chat.models import Message, ChatRoom



def run():
    room1 = ChatRoom.objects.first()
    messages = Message.objects.filter(room=room1)

    print(serializers.serialize('json', messages))


from django.core import serializers
from django.db.models import Subquery, OuterRef, Q, F, Prefetch

import json

from chat.models import Message, ChatRoom, PrivateRoom, User



def run():
    user1 = User.objects.first()

    # receiver_subquery = User.objects.filter(
    #     Q(chatroom=OuterRef('pk')) & ~Q(id=user1.id)
    # ).values('username')[:1]

    # chatrooms = user1.chatroom_set.annotate(
    #     receiver_id=Subquery(receiver_subquery)
    # )

    # print(chatrooms)

    # for room in chatrooms:
    #     print(room.receiver_id)

    chatrooms = ChatRoom.objects.filter(
        users=user1
    ).prefetch_related(
        Prefetch(
            'users',
            queryset=User.objects.exclude(id=user1.id).only("id", "username"),
            to_attr='receiver'
        )
    )

    for room in chatrooms:
        print(room.receiver_username)

    # room = ChatRoom.objects.first()

    # messages = Message.objects.filter(
    #     room=room
    # )

    # print(serializers.serialize('json', messages))
    # print(json.dumps(serializers.serialize('json', messages)))
    # print(Message.objects.filter(content="").delete())

    # room = ChatRoom.objects.last()

    # messages = Message.objects.filter(
    #     content=""
    # )
    # print(messages.delete())
    # .annotate(
    #     sender_username=F('sender__username')
    # )

    # print(serializers.serialize('json', messages))

    # for message in messages:
    #     print(message.sender_username)



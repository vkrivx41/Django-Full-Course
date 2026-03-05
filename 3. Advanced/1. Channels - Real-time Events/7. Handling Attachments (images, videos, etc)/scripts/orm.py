from django.core import serializers
from django.db.models import QuerySet, Subquery, OuterRef, Q, F, Prefetch

import json

from chat.models import Message, ChatRoom, PrivateRoom, User
from utilities.redis.presence import RedisClient


def run():
    # user1 = User.objects.first()
    # room1 = ChatRoom.objects.filter(users=user1).first()

    # print(user1, room1)
    # print(PrivateRoom.objects.get(Q(room=room1) & ~Q(user=user1)))

    # print(Message.objects.latest().attachment)
    # print(Message.objects.latest().sender)


    # serialized = serializers.serialize('json', [Message.objects.first()])
    # print(json.loads(serialized))
    
    pass
    # receiver_subquery = User.objects.filter(
    #     Q(chatroom=OuterRef('pk')) & ~Q(id=user1.id)
    # ).values('username')[:1]
    
    # chatrooms: QuerySet = user1.chatroom_set.annotate(
    #     receiver=Subquery(receiver_subquery),
    # ).values_list('receiver', flat=True)


    # receiver_subquery = User.objects.filter(
    #     Q(chatroom=OuterRef('pk')) & ~Q(id=user1.id)
    # ).values('username')[:1]
    
    # chatrooms = user1.chatroom_set.annotate(
    #     receiver_id=Subquery(receiver_subquery),
    # ).prefetch_related(
    #     Prefetch(
    #         'messages',
    #         queryset=Message.objects.filter(status=Message.MessageStatus.SENT),
    #         to_attr='unreads'
    #     )
    # )

    # receivers: list[str] = []
    # redis_client = RedisClient("localhost", 6379, 0)

    # for room in chatrooms:
    #     receivers = [*receivers, room.receiver_id]

    
    # receivers_online_status = redis_client.get_opponents_online_status(receivers)
    # result: list[dict] = []

    # for room in chatrooms:
    #     result.append({
    #         'receiver_id': room.receiver_id,
    #         'unreads': len(room.unreads),
    #         'room_name': room.room_name,
    #         'online': receivers_online_status[room.receiver_id]
    #     })

    # print(result)
    
        # chatrooms = ChatRoom.objects.filter(
        #     users=user1
        # ).prefetch_related(
        #     Prefetch(
        #         'users',
        #         queryset=User.objects.exclude(id=user1.id).only("id", "username"),
        #         to_attr='receiver'
        #     )
        # ).prefetch_related(
        #     Prefetch(
        #         'messages',
        #         queryset=Message.objects.filter(status=Message.MessageStatus.SENT),
        #         to_attr='unreads'
        #     )
        # )

    # for room in chatrooms:
    #     print(room.receiver)
    #     print(room.unreads)
    #     print(len(room.unreads))

    # room1 = ChatRoom.objects.get(room_name="room4")
    # messages = Message.objects.filter(
    #     room=room1,
    #     status=Message.MessageStatus.SENT
    # )

    # print(len(messages))

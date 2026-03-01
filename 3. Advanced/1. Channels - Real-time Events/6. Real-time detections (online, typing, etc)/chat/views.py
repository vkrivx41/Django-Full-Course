from functools import partial
import json

from django.urls import reverse_lazy
from django.views import generic, View
from django.db.models import Prefetch, OuterRef, Subquery, Q
from django.contrib.auth.views import LoginView
from django.http import JsonResponse

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination


from chat.models import User, ChatRoom, PrivateRoom, Message
from chat.serializers import MessageSerializer
from utilities.redis import presence


class UserLoginView(LoginView):
    template_name = "chat/login.html"

    success_url = reverse_lazy("chat:home")


redis_client = presence.RedisClient(
    host_name="127.0.0.1",
    port=6379,
    db_number=0
)

class HomeGeneralView(generic.TemplateView):
    template_name = "chat/chats.html"

class HomeDataView(generic.View):
    def get(self, request, *args, **kwargs):
        user = request.user

        receiver_subquery = User.objects.filter(
            Q(chatroom=OuterRef('pk')) & ~Q(id=user.id)
        ).values('username')[:1]
        
        chatrooms = user.chatroom_set.annotate(
            receiver_id=Subquery(receiver_subquery),
        ).prefetch_related(
            Prefetch(
                'messages',
                queryset=Message.objects.filter(
                    status=Message.MessageStatus.SENT
                ).exclude(sender=user),
                to_attr='unreads'
            )
        )

        receivers: list[str] = []
        redis_client = presence.RedisClient("localhost", 6379, 0)

        for room in chatrooms:
            receivers = [*receivers, room.receiver_id]

        
        receivers_online_status = redis_client.get_opponents_online_status(receivers)
        results: dict = {
            'sender': user.username,
            'data': []
        }

        for room in chatrooms:
            results['data'].append({
                'sender_id': user.id,
                'sender': user.username,
                'receiver_id': room.receiver_id,
                'unreads': len(room.unreads),
                'room_name': room.room_name,
                'online': receivers_online_status[room.receiver_id]
            })

        return JsonResponse(results)
    

class ReadMessageView(View):
    def post(self, request, *args, **kwargs):
        body = json.loads(request.body)

        target_room: str = body['room']

        unread_messages = Message.objects.filter(
            room__room_name=target_room,
            status=Message.MessageStatus.SENT
        ).exclude(sender=request.user)

        unread_count = unread_messages.update(status=Message.MessageStatus.READ)
        
        return JsonResponse({'counts': unread_count})
    

class MessageListView(generics.ListAPIView):
    queryset = Message.objects.all()

    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        current_queryset =  super().get_queryset()
        room_name = self.request.GET.get('room')

        return current_queryset.filter(
            room__room_name=room_name
        )
    

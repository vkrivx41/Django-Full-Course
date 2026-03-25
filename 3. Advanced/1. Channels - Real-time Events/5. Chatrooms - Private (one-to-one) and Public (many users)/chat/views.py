from django.urls import reverse_lazy
from django.views import generic
from django.db.models import Prefetch, OuterRef, Subquery, Q
from django.contrib.auth.views import LoginView

from functools import partial

from chat.models import User, ChatRoom, PrivateRoom


class UserLoginView(LoginView):
    template_name = "chat/login.html"

    success_url = reverse_lazy("chat:home")


class HomeListView(generic.ListView):
    context_object_name = "rooms"

    template_name = "chat/chats.html"

    def get_queryset(self):
        user = self.request.user

        # chatrooms = ChatRoom.objects.filter(
        #     users=user
        # ).prefetch_related(
        #     Prefetch(
        #         'users',
        #         queryset=User.objects.exclude(id=user.id),
        #         to_attr='receiver'
        #     )
        # )

        receiver_subquery = User.objects.filter(
            Q(chatroom=OuterRef('pk')) & ~Q(id=user.id)
        ).values('username')[:1]

        chatrooms = user.chatroom_set.annotate(
            receiver=Subquery(receiver_subquery)
        )

        return chatrooms

    
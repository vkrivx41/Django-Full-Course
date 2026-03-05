from django.contrib import admin

from chat.models import ChatRoom, PrivateRoom, Message


admin.site.register(ChatRoom)
admin.site.register(PrivateRoom)
admin.site.register(Message)


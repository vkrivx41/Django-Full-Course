from django.contrib import admin

from chat.models import ChatRoom, PrivateRoom


admin.site.register(ChatRoom)
admin.site.register(PrivateRoom)

from django.urls import re_path

from chat import consumers

websocket_urlpatterns = [
    re_path(r'presence/$', consumers.PresenceConsumer.as_asgi(), name='presence'),
    re_path(r'ws/socket/$', consumers.ChatConsumer.as_asgi(), name='create_room'),
]

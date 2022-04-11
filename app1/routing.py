from .consumer import MyasyncConsumer,windowConsumer
from django.urls import path


websocket_urlpatterns=[

    path('ws/ac/<str:room_name>/',MyasyncConsumer.as_asgi()),
    # path('ws/ac/service/<str:room_name>',windowConsumer.as_asgi()),
]

import json
from channels.generic.websocket import AsyncWebsocketConsumer # The class we're using
from asgiref.sync import sync_to_async
from channels.db import database_sync_to_async
# Implement later
from .models import *


class MyasyncConsumer(AsyncWebsocketConsumer):
  async def connect(self):
    print(self.scope)
    self.room_name = self.scope['url_route']['kwargs']['room_name']
    self.room_group_name = 'chat_%s' % self.room_name

    # Join room group
    await self.channel_layer.group_add(
      self.room_group_name,
      self.channel_name
    )


    await self.accept()
    self.accept({
    'type': 'websocket.accept'
})


    await self.send(text_data=json.dumps({
      'message':'connection establlish (from server)'
    }))

    



    

  async def disconnect(self, close_code):
    # Leave room group
    await self.channel_layer.group_discard(
      self.room_group_name,
      self.channel_name
  )

  # Receive message from WebSocket
  async def receive(self, text_data):
    data = json.loads(text_data)
    message = data['message']
    print(message)
    username = data['username']
    print(username)
    room1 = data['room']
    print(room1)

    if message == 'database':
        print('inside window')
        d=await self.save_message(username, room1, message)
        
        print('ddd',d)
        l=[]
        for i in d:
            print(i)
            l.append(i.username)
        print(l)

        for i in l:
        # Send message to room group
            await self.channel_layer.group_send(
            self.room_group_name,
            {   'type':'chat_message',
                'message': str(i),
                'username': username
            }
            )

  # Receive message from room group
  async def chat_message(self, event):
    message = event['message']
    username = event['username']

#     # Send message to WebSocket
    await self.send(text_data=json.dumps({
      'message': message,
      'username': username
    }))

  @database_sync_to_async
  def save_message(self, username, room1, message):
    try:  
        print('inside save',room1)
        obj=room.objects.get(room_name=room1)
        if obj:
            
            final=User_details.objects.filter(room=obj)
            print('this dishfds',final)
            return list(final)
    except:
        return None

  


class windowConsumer(AsyncWebsocketConsumer):
  async def connect(self):
    self.room_name = self.scope['url_route']['kwargs']['room_name']
    self.room_group_name = 'chat_%s' % self.room_name

    # Join room group
    await self.channel_layer.group_add(
      self.room_group_name,
      self.channel_name
    )

    await self.send(
      'hello this data')


    

  
  async def disconnect(self, close_code):
    # Leave room group
    await self.channel_layer.group_discard(
      self.room_group_name,
      self.channel_name
  )

  # # Receive message from WebSocket
  # async def receive(self, text_data):
  #   data = json.loads(text_data)
  #   message = data['message']
  #   username = data['username']
  #   room = data['room']

  #   await self.save_message(username, room, message)

  #   # Send message to room group
  #   await self.channel_layer.group_send(
  #     self.room_group_name,
  #     {
  #       'type': 'chat_message',
  #       'message': message,
  #       'username': username
  #     }
  #   )

  # # Receive message from room group
  # async def chat_message(self, event):
  #   message = event['message']
  #   username = event['username']

  #   # Send message to WebSocket
  #   await self.send(text_data=json.dumps({
  #     'message': message,
  #     'username': username
  #   }))

  # @sync_to_async
  # def save_message(self, username, room, message):
  #   Message.objects.create(username=username, room=room, content=message)


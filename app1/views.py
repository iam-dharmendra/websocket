from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import room
# Create your views here.

def index(request):
  return render(request, 'chat/index.html')


def room1(request, room_name):
    username = request.GET.get('username', 'Anonymous')

#   msg = room.objects.filter(room=room_name)[0:25]
    msg = room.objects.filter(room_name=room_name)
    if msg:
        pass
    else:
        r=room()
        r.room_name=room_name
        r.save()
    
    
    return render(request, 'chat/room.html', {'room_name': room_name, 'username': username})
    

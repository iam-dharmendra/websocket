from django.db import models

# Create your models here.
from django.db import models

class room(models.Model):
  room_name=models.CharField(default='',max_length=100)

  def __str__(self) -> str:
      return self.room_name



class User_details(models.Model):

  username = models.CharField(max_length=255)
  password=models.CharField(max_length=100,default='')
  room = models.ForeignKey(room,on_delete=models.CASCADE)
  uuid = models.CharField(max_length=100,default='')
  tally_key=models.CharField(max_length=100,default='')
  date_added = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ('date_added',)


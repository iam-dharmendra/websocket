from sys import displayhook
from django.contrib import admin

from app1.models import User_details, room

# Register your models here.

@admin.register(User_details)
class myadmin(admin.ModelAdmin):
    list_display=['username','id','room']


admin.site.register(room)    
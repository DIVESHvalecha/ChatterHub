from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('group_name',)

@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('group', 'user', 'message', 'timestamp')
    ordering = ('-timestamp',)
    
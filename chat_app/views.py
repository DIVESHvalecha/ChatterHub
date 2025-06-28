from django.shortcuts import render
from . import models
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'home.html')

@login_required
def group(request, group_name):
    group = models.Group.objects.filter(group_name=group_name).first()
    messages = []
    if group:
        messages = models.Message.objects.filter(group=group)
    else:
        group = models.Group.objects.create(group_name=group_name)
    return render(request, 'room.html', {'group_name': group_name, 'messages': messages})
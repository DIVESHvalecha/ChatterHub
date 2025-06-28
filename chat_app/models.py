from django.db import models
from rt_users.models import profile
# Create your models here.
class Group(models.Model):
    group_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.group_name
    
class Message(models.Model):
    group = models.ForeignKey(Group, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(profile, on_delete=models.CASCADE, null=True, related_name='messages')
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}: {self.message[:20]}..."  # Display first 20 characters of content
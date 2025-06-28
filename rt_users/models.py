from django.db import models
from cloudinary_storage.storage import MediaCloudinaryStorage

# Create your models here.

class profile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='profile')
    username = models.CharField(max_length=150, unique=True, null=True, blank=True)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True, storage=MediaCloudinaryStorage())

    def __str__(self):
        return f"{self.user.username}'s Profile"
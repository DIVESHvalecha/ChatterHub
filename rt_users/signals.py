from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from django.contrib.auth.models import User
from .models import profile as Profile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, username=instance.username)
        instance.profile.save()
        
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save() 
    
@receiver(pre_save, sender=User)
def user_presave(sender, instance, **kwargs):
    if instance.username:
        instance.username = instance.username.lower()
    
# This code listens for the post_save signal of the User model.
# When a User instance is created, it automatically creates a Profile instance linked to that user.
# It also ensures that the Profile instance is saved whenever the User instance is saved.
# This is useful for maintaining a one-to-one relationship between User and Profile models.     
# The Profile model is expected to have a one-to-one relationship with the User model,
# which is typically defined in the models.py file of the rt_users app.     
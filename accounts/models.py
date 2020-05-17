from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save 
from django.dispatch import receiver

class User(AbstractUser):
    pass

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    setting = models.IntegerField()

    def __str__(self):
        return self.user.username

# these are the signals that create a profile whenever a new user is created
@receiver(post_save, sender=User) 
def create_user_profile(sender, instance, created, **kwargs):
     if created:
         Profile.objects.create(
             user=instance,
             setting=1
             )
@receiver(post_save, sender=User) 
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
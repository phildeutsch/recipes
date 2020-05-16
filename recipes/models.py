from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from datetime import datetime
from app.helpers import RandomFileName 
from django.db.models.signals import post_save 
from django.dispatch import receiver

# Set up user and profile models
class User(AbstractUser):
    pass

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    setting = models.IntegerField()

# these are the signals that create a profile whenever a new user is created
@receiver(post_save, sender=User) 
def create_user_profile(sender, instance, created, **kwargs):
     if created:
         Profile.objects.create(user=instance, setting=1)
@receiver(post_save, sender=User) 
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

# Actual models for the app
class Dish(models.Model):
    class Meta:
        verbose_name_plural = "dishes"

    name = models.CharField(max_length=256)
    type = models.CharField(max_length=64)
    picture = models.ImageField(null=True, blank=True, upload_to=RandomFileName('dishes'))

    def __str__(self):
        return self.name

class Recipe(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    parent_recipe = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, default=None)

    created = models.DateField(auto_now_add=True)

    name = models.CharField(max_length=256)
    servings = models.IntegerField()
    ingredients = models.TextField()
    text = models.TextField()

    pinned = models.BooleanField(default=False)

    def __str__(self):
        return self.dish.name + ': ' + str(self.id)
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save 
from django.dispatch import receiver
from app.helpers import RandomFileName 
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    pass

class Profile(models.Model):
    PROFILE_PRIVACY_CHOICES = [
        (1, _('Everyone')),
        (2, _('Followers')),
        (3, _('Only you')),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    language = models.CharField(max_length=2, default='en', choices=(('en', _('English')), ('de', _('German'))))
    display_name = models.CharField(max_length=128, null=True, blank=True)
    picture = models.ImageField(null=True, blank=True, upload_to=RandomFileName('profiles'))

    privacy_recipes = models.IntegerField(choices=PROFILE_PRIVACY_CHOICES, blank=True, null=True)
    privacy_activities = models.IntegerField(choices=PROFILE_PRIVACY_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.user.username

# these are the signals that create a profile whenever a new user is created
@receiver(post_save, sender=User) 
def create_user_profile(sender, instance, created, **kwargs):
     if created:
         Profile.objects.create(
             user=instance,
             language='en',
             display_name=instance.username,
             picture=None,
             privacy_recipes=1,
             privacy_activities=1
             )
@receiver(post_save, sender=User) 
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

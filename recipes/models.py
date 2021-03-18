from django.db import models
from django.forms import ModelForm
from django.utils import timezone
from datetime import datetime
from app.helpers import RandomFileName 
from django.utils.translation import gettext_lazy as _
from simple_history.models import HistoricalRecords

from accounts.models import User

class Dish(models.Model):
    DISH_COURSE_CHOICES = [
        (1, _('First course')),
        (2, _('Main course')),
        (3, _('Dessert')),
        (4, _('Cocktail'))]
    DISH_CUISINE_CHOICES = [
        (1, _('Austrian')),
        (2, _('British')),
        (3, _('Italian')),
        (4, _('American'))
    ]

    name = models.CharField(max_length=256)
    course = models.IntegerField(choices=DISH_COURSE_CHOICES, blank=True, null=True)
    cuisine = models.IntegerField(choices=DISH_CUISINE_CHOICES, blank=True, null=True)
    picture = models.ImageField(null=True, blank=True, upload_to=RandomFileName('dishes'))

    class Meta:
        verbose_name_plural = "Dishes"

    def __str__(self):
        return self.name

class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)

    created = models.DateField(auto_now_add=True)

    name = models.CharField(max_length=256)
    servings = models.IntegerField()
    ingredients = models.TextField()
    text = models.TextField()

    history = HistoricalRecords()


    def __str__(self):
        return self.dish.name + ': ' + self.name

class Guest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    note = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Activity(models.Model):
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipes = models.ManyToManyField(Recipe)

    guests = models.ManyToManyField(Guest, blank=True)
    picture = models.ImageField(null=True, blank=True, upload_to=RandomFileName('activities'))

    class Meta: 
        verbose_name_plural = "Activities"

    def __str__(self):
        return str(self.date) + ' ' + str(self.user)

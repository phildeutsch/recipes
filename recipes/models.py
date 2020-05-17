from django.db import models
from django.utils import timezone
from datetime import datetime
from app.helpers import RandomFileName 

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
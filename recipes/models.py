from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime

class Dish(models.Model):
    class Meta:
        verbose_name_plural = "dishes"

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    type = models.CharField(max_length=64)

    def __str__(self):
        return self.name

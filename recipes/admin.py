from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Dish, Recipe

admin.site.register(Dish)
admin.site.register(Recipe)

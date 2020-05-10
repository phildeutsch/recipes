from django.contrib import admin

from .models import Dish, Recipe

admin.site.register(Dish)
admin.site.register(Recipe)

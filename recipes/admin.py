from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Dish, Recipe

admin.site.register(User, UserAdmin)
admin.site.register(Dish)
admin.site.register(Recipe)

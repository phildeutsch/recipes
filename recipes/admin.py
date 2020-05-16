from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile, Dish, Recipe

admin.site.register(User, UserAdmin)
admin.site.register(Profile)
admin.site.register(Dish)
admin.site.register(Recipe)

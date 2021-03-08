from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Dish, Recipe, Guest, Activity

admin.site.register(Dish)
admin.site.register(Recipe)
admin.site.register(Guest)
admin.site.register(Activity)

from django import forms
from django.forms import ModelForm
from .models import Dish, Recipe, Guest, Activity

class DishForm(ModelForm):
    class Meta:
        model = Dish
        exclude = ['user', 'picture']

class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'servings', 'ingredients', 'text']

class GuestForm(ModelForm):
    class Meta:
        model = Guest
        exclude = ['user']

class ActivityForm(ModelForm):
    class Meta:
        model = Activity
        exclude = ['user', 'datetime']
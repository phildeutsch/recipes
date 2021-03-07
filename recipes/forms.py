from django import forms
from django.forms import ModelForm
from .models import Dish, Recipe

class DishForm(ModelForm):
    class Meta:
        model = Dish
        exclude = ['user', 'picture']

class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'servings', 'ingredients', 'text']
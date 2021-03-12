from django import forms
from django.forms import ModelForm
from .models import Dish, Recipe, Guest, Activity
from django.utils.translation import ugettext_lazy as _

class DishForm(ModelForm):
    class Meta:
        model = Dish
        exclude = ['user', 'picture']
        labels = {
            "name": _("Name"),
            "course": _("Course"),
            "cuisine": _("Cuisine")
        }


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'servings', 'ingredients', 'text']

class GuestForm(ModelForm):
    class Meta:
        model = Guest
        exclude = ['user']
        labels = {
            "name": _("Name"),
            "note": _("Note")
        }

class ActivityForm(ModelForm):
    class Meta:
        model = Activity
        exclude = ['user', 'datetime']
        labels = {
            "recipes": _("Recipes"),
            "guests": _("Guests"),
            "picture": _("Picture"),
        }

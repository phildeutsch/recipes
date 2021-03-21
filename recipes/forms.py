from django import forms
from django_select2 import forms as s2forms
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
        exclude = ['user', 'dish', 'created', 'history']

class GuestForm(ModelForm):
    class Meta:
        model = Guest
        exclude = ['user']
        labels = {
            "name": _("Name"),
            "note": _("Note")
        }


class RecipeWidget(s2forms.ModelSelect2MultipleWidget):
    search_fields = [
        "name__icontains"
    ]
class GuestWidget(s2forms.ModelSelect2MultipleWidget):
    search_fields = [
        "name__icontains"
    ]

class ActivityForm(ModelForm):
    class Meta:
        model = Activity
        exclude = ['user']
        labels = {
            "recipes": _("Recipes"),
            "guests": _("Guests"),
            "picture": _("Picture"),
        }
        widgets = {
            "recipes": RecipeWidget,
            "guests": GuestWidget,
        }
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(ActivityForm, self).__init__(*args, **kwargs)
        self.fields['guests'].queryset = Guest.objects.filter(user=user)
        self.fields['recipes'].queryset = Recipe.objects.filter(user=user)

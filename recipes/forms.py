from django import forms
from django.forms import ModelForm
from .models import Dish, Recipe, ARTEN_CHOICE

class DishForm(ModelForm):
    class Meta:
        model = Dish
        exclude = ['user']
#class DishForm(forms.Form):
#    name = forms.CharField(max_length=256)
#    type = forms.CharField(
#        max_length = 64,
#        widget=forms.Select(choices=ARTEN_CHOICE),
#    )
#    cat_ingredients = forms.CharField(max_length=80)
#    etno = forms.CharField(max_length=80)

    def __init__(self, *args, **kwargs):
        super(DishForm, self).__init__(*args, **kwargs)
        self.fields['picture'].required = False

class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'servings', 'ingredients', 'text']
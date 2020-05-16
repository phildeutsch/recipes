from django.forms import ModelForm
from .models import User, Dish, Recipe
from django_registration.forms import RegistrationForm

class UserForm(RegistrationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class DishForm(ModelForm):
    class Meta:
        model = Dish
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super(DishForm, self).__init__(*args, **kwargs)
        self.fields['picture'].required = False

class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'servings', 'ingredients', 'text']
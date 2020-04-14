from django.forms import ModelForm
from .models import Dish

class DishForm(ModelForm):
    class Meta:
        model = Dish
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super(DishForm, self).__init__(*args, **kwargs)
        self.fields['picture'].required = False
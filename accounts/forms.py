from django.forms import ModelForm
from .models import User
from django_registration.forms import RegistrationForm

class UserForm(RegistrationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

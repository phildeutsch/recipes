from django.forms import ModelForm
from .models import User, Profile
from django_registration.forms import RegistrationForm

class UserForm(RegistrationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

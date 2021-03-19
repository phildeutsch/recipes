from django.forms import ModelForm
from .models import User, Profile
from django_registration.forms import RegistrationForm
from django.utils.translation import ugettext_lazy as _

class UserForm(RegistrationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        labels = {
            "language": _("Language"),
            "display_name": _("Display Name"),
            "picture": _("Picture"),
            "privacy_recipes": _("Privacy Recipes"),
            "privacy_activities": _("Privacy Activities")
        }


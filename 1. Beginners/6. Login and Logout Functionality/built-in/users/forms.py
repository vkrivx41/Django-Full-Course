from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, max_length=50)

    class Meta:
        model = User  # the DB model to save the data to
        fields = ["username", "email", "password1", "password2"]

        # the fields list designates the order the fields will be arranged into
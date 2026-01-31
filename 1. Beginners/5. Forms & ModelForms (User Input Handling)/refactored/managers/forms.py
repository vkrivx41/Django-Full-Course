from django import forms

from .models import Manager


from .choices import PermissionChoices

class ManagerForm(forms.ModelForm):
    permissions = forms.MultipleChoiceField(
        choices=PermissionChoices.choices,
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Manager
        fields = ["username", "email", "phone_number", "permissions"]

        widget: dict = {
            'username': forms.TextInput(attrs={'placeholder': "Enter the username."}),
            'email': forms.EmailInput(attrs={'placeholder': "Enter the email."}),
            'phone_number': forms.TextInput(attrs={'placeholder': "Enter the phone number."}),
        }
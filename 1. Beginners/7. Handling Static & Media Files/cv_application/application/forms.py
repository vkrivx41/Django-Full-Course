from django import forms

from .models import CV
from .choices import TitleChoices


class CVForm(forms.ModelForm):
    title = forms.ChoiceField(choices=TitleChoices.choices)

    class Meta:
        model = CV
        fields = ['name', 'title', 'resume']

        widgets: dict = {
            'resume': forms.FileInput(attrs={'accept': '.jpg,.png,.pdf'})
        }
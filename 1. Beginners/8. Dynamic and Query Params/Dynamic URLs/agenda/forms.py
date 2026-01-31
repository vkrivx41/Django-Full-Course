from django import forms

from .models import Agenda
from .choices import AgendaTypeChoices, AgendaColorChoices

from datetime import date, timedelta


class AgendaForm(forms.ModelForm):
    type = forms.ChoiceField(choices=AgendaTypeChoices.choices)
    color = forms.ChoiceField(choices=AgendaColorChoices.choices)

    class Meta:
        model = Agenda
        fields: list = ['name', 'description', 'type', 'color', 'due_date']

        widgets: dict = {
            'due_date': forms.DateInput(attrs={'type': 'date', 'min': date.today() + timedelta(days=1)})
        }


class AgendaEditForm(forms.ModelForm):
    type = forms.ChoiceField(choices=AgendaTypeChoices.choices)
    color = forms.ChoiceField(choices=AgendaColorChoices.choices)
    
    class Meta:
        model = Agenda
        fields: list = ['name', 'description', 'type', 'color', 'due_date', 'accomplished']

        widgets: dict = {
            'due_date': forms.DateInput(attrs={'type': 'date', 'min': date.today() + timedelta(days=1)}),
            'accomplished': forms.CheckboxInput()
        }
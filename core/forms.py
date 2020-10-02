from django import forms
from .models import Company
from django.forms.widgets import ClearableFileInput


class CustomFileInput(ClearableFileInput):
    initial_text = 'Atual'
    input_text = 'Trocar para '
    clear_checkbox_label = 'Limpar'


class FormCompany(forms.ModelForm):
    logo = forms.ImageField(label=None, required=False, widget=CustomFileInput)

    class Meta:
        model = Company
        fields = ['name', 'legal_number', 'logo']

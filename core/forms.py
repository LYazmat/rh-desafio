from django import forms
from .models import Company, Department, Employee
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


class FormDepartment(forms.ModelForm):

    class Meta:
        model = Department
        fields = ['name', 'status', 'admin', 'company']
        widgets = {
            'status': forms.CheckboxInput,
        }

    def __init__(self, *args, **kwargs):
        super(FormDepartment, self).__init__(*args, **kwargs)
        self.fields['company'].empty_label = 'Selecione uma empresa'
        self.fields['company'].label = 'Empresa'
        self.fields['admin'].empty_label = 'Selecione o Administrador'
        self.fields['admin'].label = 'Administador'


class FormEmployee(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ['department', 'name', 'user', 'gender', 'role', 'phone', 'age', 'joining_date', 'salary', 'email']
        widgets = {
            'joining_date': forms.TextInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(FormEmployee, self).__init__(*args, **kwargs)
        self.fields['department'].empty_label = 'Selecione um departamento'
        self.fields['department'].label = 'Departamento'
        self.fields['user'].empty_label = 'Selecione o usuário'
        self.fields['user'].label = 'Usuário'


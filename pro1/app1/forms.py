from django import forms
from .models import Client

s = [
    ('Onboarded', 'Onboarded'),
    ('Not Onboarded', 'Not Onboarded'),
]

d = [
    ('SAAS', 'SAAS'),
    ('Ecommerce', 'Ecommerce'),
    ('CRM', 'CRM'),
    ('ERP', 'ERP'),
    ('Finance', 'Finanace'),
]

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

        labels = {
            'id' : 'Client ID',
            'name' : 'Client Name',
            'email' : 'Email ID',
            'dept' : 'Department',
            'doj' : 'Date of Joining',
            'domain' : 'Project Domain',
        }

        widgets = {
            'id': forms.NumberInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'company': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'dept': forms.TextInput(attrs={'class': 'form-control'}),
            'doj': forms.DateInput(attrs={'class': 'form-control', 'type':'date'}),
            'status': forms.Select(choices=s, attrs={'class': 'form-control'}),
            'domain': forms.SelectMultiple(choices=d, attrs={'class': 'form-control'}),
        }
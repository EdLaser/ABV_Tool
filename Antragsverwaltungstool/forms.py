from django.forms import ModelForm
from django import forms
from Antragsverwaltungstool.models import Universall


class NewUniversallForm(ModelForm):
    #file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    class Meta:
        model = Universall
        exclude = ['flag', 'number', 'date']
    
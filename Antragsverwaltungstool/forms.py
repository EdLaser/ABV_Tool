from django.forms import ModelForm

from Antragsverwaltungstool.models import Universall


class NewUniversallForm(ModelForm):
    class Meta:
        model = Universall
        exclude = ['flag', 'number', 'date']



from django import forms
from . models import PlasmaXchange
from django.forms.models import ModelForm

class plasmaxchangeForm(ModelForm):
    PatientName = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control',}
        ))
    DonorName = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control',}
        ))

    class Meta:
        model=PlasmaXchange
        fields=('PatientName','DonorName')
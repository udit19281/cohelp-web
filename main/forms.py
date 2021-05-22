from django import forms
from .models import PlasmaXchange,RequestedResource
from django.forms.models import ModelForm

class plasmaxchangeForm(ModelForm):
    class Meta:
        model = PlasmaXchange
        fields='__all__'
        exclude=('status',)


class RequestedResourceForm(ModelForm):

    class Meta:
        model=RequestedResource
        fields='__all__'
        exclude=('status',)
        # widgets=forms.Select(attrs={'class': 'form-control',})
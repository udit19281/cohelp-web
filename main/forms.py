from django import forms
from .models import PlasmaXchange, RequestedResource, VolunteerRequest
from django.forms.models import ModelForm
from django.forms.widgets import Textarea

class plasmaxchangeForm(ModelForm):
    class Meta:
        model = PlasmaXchange
        fields='__all__'
        exclude=('status',)

class RequestedResourceForm(ModelForm):

    class Meta:
        model=RequestedResource
        fields='__all__'
        exclude=('status','reply')
        # widgets=forms.Select(attrs={'class': 'form-control',})

class contactform(forms.Form):
    name = forms.CharField(label="Your Name", max_length=50)
    email=forms.EmailField(label="Email",max_length=50)
    number=forms.CharField(label="Number",max_length=10)
    # message = forms.CharField(label="Message",max_length=255)
    # message= forms.CharField(widget= forms.TextInput(attrs={'class':'form-input'}))
    message = forms.CharField( widget=forms.Textarea(attrs={'rows':'5'}) )
    class Meta:
        fields=['name','email','message']
        # widgets = {
        #     'message': Textarea(attrs={'cols': 80, 'rows': 20}),
        # }
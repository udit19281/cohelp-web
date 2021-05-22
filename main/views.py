from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse, HttpResponseRedirect
from main.models import User
from django.db import IntegrityError
from django.urls import reverse
from .forms import plasmaxchangeForm
# Create your views here.

def index(request):
    return render(request,"home.html")



def plasmaxchange(request):
    form = plasmaxchangeForm()
    if request.method =='POST':
        form = plasmaxchangeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Form Received")
    context={
        'form':form
    }
    return render(request,"plasmaxchange.html",context)
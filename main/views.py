from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse, HttpResponseRedirect
from main.models import User
from django.db import IntegrityError
from django.urls import reverse
from .forms import plasmaxchangeForm
# Create your views here.
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request,"home.html")


@login_required(login_url="authentication:login")
def dashboard(request):
    return render(request,"dashboard.html")

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
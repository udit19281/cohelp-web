from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse, HttpResponseRedirect
from main.models import User
from django.db import IntegrityError
from django.urls import reverse
from django.contrib import messages
from .forms import *
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render


def index(request):
    return render(request,"home.html")

def blog(request):
    return render(request,"blog.html")

def mission(request):
    return render(request,"mission.html")

def workshop(request):
    return render(request,"workshop.html")


@login_required(login_url="authentication:login")
def dashboard(request):
    return render(request,"dashboard.html")

@login_required(login_url="authentication:login")
def form(request,name):
    print(request.method)
    if request.method =='GET':
        if(name=="resources"):
            form = RequestedResourceForm()
            context={
        'formname':'resources',
        'form':form }
            return render(request,"form.html",context)
        elif (name=="plasmaxchange"):
            form = plasmaxchangeForm()
            context={
        'formname':'plasmaxchange',
        'form':form}
        return render(request,"form.html",context)
    if request.method == 'POST':
        if(name=="resources"):
           form=RequestedResourceForm(request.POST)
           if form.is_valid():
                form.save()
                messages.success(request,"Form has been submitted successfully")
                return redirect("main:dashboard")

        if(name=="plasmaxchange"):
           form=plasmaxchangeForm(request.POST)
           if form.is_valid():
                form.save()
                messages.success(request,"Form has been submitted successfully")
                return redirect("main:dashboard")
    messages.error(request,"Invalid form!")
    return redirect("main:dashboard")  
        


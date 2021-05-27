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
from django.core.mail import send_mail
from decouple import config
from .models import *

def index(request):
    return render(request,"home.html")

def blog(request):
    return render(request,"blog.html")

def mission(request):
    return render(request,"mission.html")

def workshop(request):
    return render(request,"workshop.html")

def founders(request):
    return render(request,"founders.html")

def volunteer(request):
    return render(request,"volunteer.html")
def backToSchool(request):
    return render(request,"backToSchool.html")

def contact(request):
    form=contactform()
    if request.method == 'POST':
        form=contactform(request.POST)
        if form.is_valid():
            name=form.cleaned_data["name"]
            message=form.cleaned_data["message"]
            number=form.cleaned_data["number"]
            email=form.cleaned_data["email"]
            if name!="" and message!="" and email!="" and message!="" and number.isnumeric():
               subject="New Contact request from "+name
               body="Here is the message \n"+ message+"\n"+"Number: "+number+"\n"+"Email: "+email
               print(body)
               hostuser=config('EMAIL_HOST_USER')
               sendto=config('EMAIL_REC')
               print(sendto,hostuser)
               send_mail(subject,body,hostuser,[sendto],fail_silently=False,)
               messages.success(request,"Your message has been sent successfully!")
               return render(request,"home.html")
        messages.error(request,"Please enter correct input")
        return render(request,"home.html")
    else:
        return render(request,"contact.html",context={"form":form})

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



        
def showresource(request):
    content=AddResource.objects.exclude(name="NA")
    context={
        'content':content
    }
    return render(request,"resource.html",context=context)


def resourcetable(request,id):
    tablename=AddResource.objects.get(id=id)
    gettable=ResourceTable.objects.filter(resource_name=tablename)
    gettable=gettable.exclude(status="Pending")
    
    print(gettable)
    context={
        "name":tablename,
        "content":gettable
    }
    return render(request,"resourcetable.html",context=context)
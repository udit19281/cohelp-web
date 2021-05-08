from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse, HttpResponseRedirect
from main.models import User
from django.db import IntegrityError
from django.urls import reverse
# Create your views here.

def index(request):
    return render(request,"index.html")

def login_user(request):
    if request.method =="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse("main:index"))
        else: return HttpResponse("Wrong username or password!")
    return render(request,"registration/login.html")

def register(request):
    if request.method == "POST":
        usernam = request.POST.get("username")
        passwor = request.POST.get("password")
        emai = request.POST.get("email")
        confirmatio = request.POST.get("confirmation")

        if passwor!=confirmatio:
            return HttpResponse("Password does not match!")
        try:
            user=User.objects.create_user(username=usernam,password=passwor,email=emai)
            user.save()
        except IntegrityError:
            return HttpResponse("Username already taken :(")
        login(request,user)
        return HttpResponse("Logged in successfully")

    return render(request,"registration/register.html")

def logout_user(request):
    logout(request)
    return render(request,"index.html")
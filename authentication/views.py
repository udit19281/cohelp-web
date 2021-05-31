from django.shortcuts import redirect, render
import json
from django.views.generic import View
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from validate_email import validate_email
from django.contrib import auth, messages
import re
from django.core.mail import send_mail
import os
# from twilio.rest import Client
from decouple import config
from .utils import account_activation_token
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.urls.base import reverse
from main.models import Profile
# Create your views here.
User=get_user_model()

def signup(request):
    if request.method == 'POST':
        
        email=request.POST['email']
        password=request.POST['password']
        username=request.POST['username']
        phonenumber=request.POST['phonenumber']
        context={
            "fieldvalue":request.POST
        }
        if username=="" or password=="" or email=="" or not phonenumber.isnumeric():
            messages.error(request,"Invalid Fields!!!")
            return render(request,'auth/signup.html')
        phonenumber="+91"+phonenumber
        if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=email).exists():
                user=User.objects.create_user(username=username,email=email, password=password)
                user.is_active=False
                profile=Profile.objects.create(user=user)
                profile.number=phonenumber
                #send verification mail
                current_site=get_current_site(request)
                uid=urlsafe_base64_encode(force_bytes(user.pk))
                token=account_activation_token.make_token(user)
                link=reverse('authentication:activate',kwargs={'uid':uid, 'token':token})
                acti_url="http://"+current_site.domain+link
                subject="Activate your account"
                body="Hello "+user.username+", Here is your activation link \n"+acti_url
                send_mail(
                     subject,
                        body,
                        'noreply@uditorg.com',
                    [email],
                    fail_silently=False,
                )
                #SMS part
                # try:
                #     account_sid =config('TWILIO_ACCOUNT_SID')
                #     auth_token = config('TWILIO_AUTH_TOKEN')
                #     client=Client(account_sid,auth_token)
                #     message=client.messages.create(
                #         body=body,
                #         from_="+1506596",
                #         to=phonenumber
                #     )
                #     print(message.sid)
                # except Exception as e:
                #     print(e)
                profile.save()
                user.save()
                messages.success(request,"Account Created Successfully, Please check your email for verification.")
                return render(request,'auth/signup.html')
            messages.error(request,"User Account Already exists!!!")
            return render(request,'auth/signup.html',context)
        messages.error(request,"Username Already Exists!!!")
        return render(request,'auth/signup.html',context)
    return render(request,'auth/signup.html')

def reset(request):
    if request.method == 'POST':

        
        return render(request,'auth/login.html')
    return render(request,'auth/reset.html')


class ValidateEmail(View):
    def post(self, request):
        data=json.loads(request.body)
        email=data['email']
        if not validate_email(email):
            return JsonResponse({'email_error':'Email is invalid'},status=400)
        if User.objects.filter(email=email,is_active=True).exists():
            return JsonResponse({'email_error':'email_already exists!'},status=400)
        return JsonResponse({'email_valid':True})

class ValidateUsername(View):
    def post(self,request):
        
        data=json.loads(request.body)
        # print(data)
        username=data['username']
        if User.objects.filter(username=username,is_active=True).exists():
            return JsonResponse({'username_error':'username already exists!'},status=400)
        return JsonResponse({'username_valid':True})

class activate(View):
    def get(self,request,uid,token):
        try:
            id=force_text(urlsafe_base64_decode(uid))
            user=User.objects.get(pk=id)
            if not account_activation_token.check_token(user,token):
                return redirect('authentication:login')
            if user.is_active:
                return redirect('authentication:login')
            user.is_active=True
            user.save()
            messages.success(request,"Account Activated")
            return redirect('authentication:login')
        except Exception as e:
            messages.error(request,"Something went wrong")
            return redirect('authentication:login')

class Login(View):
    def get(self,request):
        return render(request, 'auth/login.html')

    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']

        if username!=None and password!=None:
            user=auth.authenticate(username=username,password=password)

            if user:
                if user.is_active:
                    auth.login(request,user)
                    messages.success(request,"Welcome "+username+", You have been Authenticated successfully!")
                    return redirect('main:dashboard')
                else:
                    messages.error(request,"Account is not active!")
                    return render(request,'auth/login.html')
            messages.error(request,"Invalid credentials!")
            return redirect('authentication:login')
        messages.error(request,"Invalid Fields!")
        return redirect('authentication:login')

class Logout(View):
    def post(self,request):
        auth.logout(request)
        messages.success(request,"You have been logged out")
        return redirect('main:home')

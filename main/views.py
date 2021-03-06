from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse, HttpResponseRedirect
from main.models import User
from django.db import IntegrityError
from django.urls import reverse
from django.contrib import messages
from .forms import *
import csv
from django.http import Http404
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.core.mail import send_mail
from decouple import config
from .models import *
from django.core.paginator import Paginator

def index(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")

def communityKitchen(request):
    return render(request,"community.html")

def blog(request):
    return render(request,"blog.html")

def mission(request):
    return render(request,"mission.html")

def workshop(request):
    return render(request,"workshop.html")

def founders(request):
    return render(request,"founders.html")

def backToSchool(request):
    return render(request,"backToSchool.html")

def helpBuddies(request):
    return render(request,"help_buddies.html")

def projectSlum(request):
    return render(request,"project_slum.html")

# @login_required(login_url="authentication:login")
def collaborate(request):
    if request.method == 'POST':
        username = request.POST['username']
        number = request.POST['contact']
        reason=request.POST['reason']
        exp=request.POST['experience']
        if number!='' and reason!='' and exp!='':
            NewCollaboratorRequest.objects.create(username=username,number=number,reason=reason,experience=exp)
            messages.success(request,"Collaborator form has been sent successfully!!! ")
            return redirect("main:home")
        else:
            messages.error(request,"Error!!!, Enter all fields")
            return redirect("main:home")
    else:
        return render(request,"collaborate.html")


@login_required(login_url="authentication:login")
def volunteer(request):
    if request.method == 'POST':
        username = request.user.username
        number = request.POST['contact']
        roll=request.POST['field']
        exp=request.POST['experience']
        if number!='' and roll!='' and exp!='':
            # print(username,number,roll,exp)
            VolunteerRequest.objects.create(username=username,number=number,roll=roll,experience=exp)
            messages.success(request,"Volunteer form has been sent successfully!!! ")
            return redirect("main:home")
        else:
            messages.error(request,"Error!!!, Enter all fields")
            return redirect("main:home")
    else:
        return render(request, "volunteer.html")

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
    user=request.user
    if user.is_staff and user.is_active:
        if user.is_superuser:
            context={"staff":True,"admin":True}
        else:
            context={'staff':True}
        return render(request,"dashboard.html",context=context)
    else:
        request_res=RequestedResource.objects.filter(username=user)
        request_plasma=PlasmaXchange.objects.filter(username=user)
        context = {}
        if request_res and request_plasma:
            context['resource'] = request_res
            context['plasma'] = request_plasma
        elif request_plasma:
            context={'plasma' : request_plasma}
        elif request_res:
            context['resource'] = request_res
        else:
            context['text'] = 'Requested forms will be shown here'
        print(context)
        return render(request,"dashboard.html",context=context)

@login_required(login_url="authentication:login")
def form(request,name):
    if request.method =='GET':
        if(name==1):
            form = RequestedResourceForm()
            context={
                'formid':1,
        'formname':'resources',
        'form':form }
            return render(request,"form.html",context)
        elif (name==2):
            form = plasmaxchangeForm()
            context={
                'formid':2,
        'formname':'plasmaxchange',
        'form':form}
            return render(request,"form.html",context)
        elif (name==3):
            form = ResourceTableForm()
            context={
                'formid':3,
        'formname':'addresource',
        'form':form}
            return render(request,"form.html",context)

    if request.method == 'POST':
        if(name==1):
           form=RequestedResourceForm(request.POST)
           if form.is_valid():
                data=form.save(commit=False)
                data.username=request.user
                form.save()
                messages.success(request,"Form has been submitted successfully")
                return redirect("main:dashboard")

        elif(name==2):
           form=plasmaxchangeForm(request.POST)
           if form.is_valid():
                data=form.save(commit=False)
                data.username=request.user
                form.save()
                messages.success(request,"Form has been submitted successfully")
                return redirect("main:dashboard")

        elif(name==3):
           form=ResourceTableForm(request.POST)
           if form.is_valid():
                # data=form.save(commit=False)
                # data.username=request.user
                form.save()
                messages.success(request,"Form has been submitted successfully,Verification pending")
                return redirect("main:dashboard")
    print(name,type(name),name==1)
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
    paginator=Paginator(gettable,50)
    pagenum=request.GET.get('page')
    gettable=Paginator.get_page(paginator,pagenum)
    context={
        "name":tablename,
        "content":gettable
    }
    return render(request,"resourcetable.html",context=context)


@login_required(login_url="authentication:login")
def exportdata(request,id):
    if not request.user.is_superuser:
        raise Http404()
    else:
        response =HttpResponse(content_type='text/csv')
        if id==1:
            response['Content-Disposition']='attachment; filename=Resource_Request'+str(datetime.datetime.now())+'.csv'
            write=csv.writer(response)
            write.writerow(['Username','Resource Requested','Contact Number','Status','Description','Comment'])
            data=RequestedResource.objects.all()
            for i in data:
                write.writerow([i.username,i.resource,i.number,i.status,i.description,i.reply])
            return response
        if id==2:
            response['Content-Disposition']='attachment; filename=Plasma_Request'+str(datetime.datetime.now())+'.csv'
            write=csv.writer(response)
            write.writerow(['Username','Patient Name','Patient Age','Status','Patient Blood Group','Patient Contact','Patient Address','Donor Name','Donor Age','Donor Blood Group','Donor Contact','Donor Address'])
            data=PlasmaXchange.objects.all()
            for i in data:
                write.writerow([i.username,i.Patient_Name,i.Patient_Age,i.status,i.Patient_Blood_Group,i.Patient_Contact,i.Patient_Address,i.Donor_Name,i.Donor_Age,i.Donor_Blood_Group,i.Donor_Contact,i.Donor_Address])
            return response
        else:
            raise Http404()
        


#id form name
#1  reuest resource
#2  plasma x change 
#3 add resource form
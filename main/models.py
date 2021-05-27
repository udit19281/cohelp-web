#from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model
from django.db import models
import datetime
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import send_mail

# Create your models here.

class Profile(models.Model):
   user=models.ForeignKey(to=User,on_delete=models.CASCADE)
   number=models.CharField(max_length=13)

   def __str__(self):
      return self.user.username+"'s profile"

cho_status2=[
      ('Pending', 'Pending'),
      ('Verified','Verified'),
      ('Not Available','Not Available'),
      ('Ok','Ok'),
   ]

User_obj=get_user_model()

class PlasmaXchange(models.Model):
   username= models.CharField(max_length=255,default="NA") #exclude in form
   Patient_Name = models.CharField(max_length=500)
   Patient_Age = models.IntegerField()
   Patient_Blood_Group = models.CharField(max_length=3)
   Patient_Contact = models.CharField(max_length=15)
   Patient_Address = models.CharField(max_length=200)
   # donor fiels
   Donor_Name = models.CharField(max_length=50)
   Donor_Age = models.IntegerField()
   Donor_Blood_Group = models.CharField(max_length=3)
   Donor_Contact = models.CharField(max_length=15)
   Donor_Address = models.CharField(max_length=200)
   status=models.CharField(choices=cho_status2,default="Pending",max_length=50)
   
   class Meta:
      db_table = "Plasmaxchange"

   def __str__(self):
      return "Applicant "+self.username +", status "+self.status+",donar: "+self.Donor_Name


class RequestedResource(models.Model):
   username=models.CharField(max_length =50) #exclude in form
   resource = models.ForeignKey('AddResource', on_delete=models.CASCADE)
   number = models.CharField(max_length =50,default="NA")
   description = models.CharField(max_length=255,default="NA")
   status=models.CharField(choices=cho_status2,default="Pending",max_length=50)  #exclude in form
   reply=models.CharField(max_length=255,null=True,blank=True) #volunteer reply to be sent
   class Meta:
      db_table = "RequestedResource"

   def __str__(self):
      return self.resource.name+" Requested By "+self.username+", status "+self.status

class AddResource(models.Model):       #For admin only
   name= models.CharField(max_length=255,default="NA")
   description=models.TextField(max_length=255,default="NA")
   image_url=models.TextField(max_length=255,default="NA")
   
   def __str__(self):
      return self.name


class VolunteerRequest(models.Model):
   username = models.CharField(max_length=255, default="NA")
   number = models.CharField(max_length=50, default="NA")
   roll = models.CharField(max_length=50, default="NA")
   experience = models.TextField(max_length=255,default="NA")
   status = models.CharField(choices=cho_status2,default="Pending",max_length=50)  #exclude in form
   reply=models.CharField(max_length=255,default="NA")
   def __str__(self):
      return self.username

class ResourceTable(models.Model):
   resource_name=models.ForeignKey(AddResource, on_delete=models.CASCADE)
   # resource_name = models.CharField(max_length=255,default="NA")
   org_name = models.CharField(max_length=255,default="NA")
   number=models.CharField(max_length=25,default="NA")
   address = models.CharField(max_length=255,default="NA")
   contact_person = models.CharField(max_length =100,default="NA")
   quantity=models.CharField(max_length=100,default="NA")
   status=models.CharField(choices=cho_status2,default="Pending",max_length=50)  #exclude in form
   link=models.CharField(max_length=255,default="NA")
   created_on=  models.DateField(default=datetime.datetime.now)   #exclude in form
   last_updated= models.DateField(blank=True,null=True)  #exclude in form
   description=models.TextField(max_length=555,default="NA")

   def __str__(self):
      return self.resource_name.name+" by "+self.org_name


   class Meta:
      ordering = ('-created_on','-last_updated')


# Signals

@receiver(post_save,sender=RequestedResource)
def send_mail_user_status_update(sender,instance,created,*args,**kwargs):

   if instance.status!='Pending':
      if User.objects.filter(username=instance.username).exists():
         user=User.objects.get(username=instance.username)
         email=user.email
         subject="Status Update on Mango"
         body="Hello, "+str(user.username)+"\nYour Request Status has been updated \n"+"Status: "+instance.status+"\n"+"reply: "+str(instance.reply)
         send_mail(subject,body,'noreply@uditorg.com', [email],fail_silently=False,)
         print("email sent")

@receiver(post_save,sender=VolunteerRequest)
def send_mail_user_status_update(sender,instance,created,*args,**kwargs):

   if instance.status!='Pending':
      if User.objects.filter(username=instance.username).exists():
         user=User.objects.get(username=instance.username)
         email=user.email
         subject="Volunteer Status Update on Mango"
         body="Hello, "+str(user.username)+"\nYour Volunteer request Status has been updated \n"+"Status: "+instance.status+"\n"+"reply: "+str(instance.reply)
         send_mail(subject,body,'noreply@uditorg.com', [email],fail_silently=False,)
         print("Volunteer email sent")
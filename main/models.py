#from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model
from django.db import models
import datetime

# Create your models here.


cho_status2=[
      ('Pending', 'Pending'),
      ('Verified','Verified'),
      ('Not Available','Not Available'),
      ('Ok','Ok'),
   ]

class User(AbstractUser):
   phonenumber = models.CharField(max_length=13,default="NA")
   volunteer = models.BooleanField(default=False)

User_obj=get_user_model()

class PlasmaXchange(models.Model):
   userename= models.CharField(max_length=255,default="NA") #exclude in form
   PatientName = models.CharField(max_length=500,name="Patient Name")
   PatientAge = models.IntegerField(name="Patient Age")
   PatientBloodGroup = models.CharField(max_length=3,name="Patient Blood Group")
   PatientContact = models.IntegerField(name="Patient Contact")
   PatientAddress = models.CharField(max_length=200,name="Patient Address")
   # donor fiels
   DonorName = models.CharField(max_length=50,name="Donor Name")
   DonorAge = models.IntegerField(name="Donor Age")
   DonorBloodGroup = models.CharField(max_length=3,name="Donor Blood Group")
   DonorContact = models.IntegerField(name="Donor Contact")
   DonorAddress = models.CharField(max_length=200,name="Donor Address")
   status=models.CharField(choices=cho_status2,default="Pending",max_length=50)
   
   class Meta:
      db_table = "Plasmaxchange"

   def __str__(self):
      return "Applicant "+self.username +", status "+self.status


class RequestedResource(models.Model):
   username=models.CharField(max_length =50) #exclude in form
   resource = models.CharField(max_length=50,default="NA")
   number = models.CharField(max_length =50,default="NA")
   description = models.CharField(max_length=255,default="NA")
   status=models.CharField(choices=cho_status2,default="Pending",max_length=50)  #exclude in form

   class Meta:
      db_table = "RequestedResource"

   def __str__(self):
      return self.resource+" Requested By "+self.username+", status "+self.status

class ResourceTable(models.Model):
   resource_name = models.CharField(max_length=255,default="NA")
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
      return self.resource_name+" by "+self.org_name


   class Meta:
      ordering = ('-created_on','-last_updated')


class AddResource(models.Model):       #For admin only
   name= models.CharField(max_length=255,default="NA")
   description=models.TextField(max_length=255,default="NA")
   image_url=models.TextField(max_length=255,default="NA")

   def __str__(self):
      return self.name

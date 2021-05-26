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
   username= models.CharField(max_length=255,default="NA") #exclude in form
   Patient_Name = models.CharField(max_length=500)
   Patient_Age = models.IntegerField()
   Patient_Blood_Group = models.CharField(max_length=3)
   Patient_Contact = models.IntegerField()
   Patient_Address = models.CharField(max_length=200)
   # donor fiels
   Donor_Name = models.CharField(max_length=50)
   Donor_Age = models.IntegerField()
   Donor_Blood_Group = models.CharField(max_length=3)
   Donor_Contact = models.IntegerField()
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




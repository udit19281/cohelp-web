from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model

# Create your models here.


class User(AbstractUser):
    pass

User_obj=get_user_model()

class Oxygen(models.Model):

   name = models.CharField(max_length = 50, default="NA")
   contact_number = models.IntegerField()
   area = models.CharField(max_length =200, default="NA")
   contact_person = models.CharField(max_length =100, default="NA")
   status = models.CharField(max_length = 50,default="NA")
   last_verified=  models.DateField()
   
   class Meta:
      db_table = "Oxygen"

class FoodSupport(models.Model):

   name = models.CharField(max_length = 50)
   contact_number = models.IntegerField()
   contact_person = models.CharField(max_length =100,default="NA")
   address = models.CharField(max_length = 70,default="NA")
   status=models.CharField(max_length = 100,default="NA")
   no_of_meals = models.IntegerField(default=0)
   verified = models.BooleanField(default=False)

   class Meta:
      db_table = "Foodsupport"

class Ambulance(models.Model):

   name = models.CharField(max_length = 50)
   contact_number = models.IntegerField()
   contact_person = models.CharField(max_length =100,default="NA")
   address = models.CharField(max_length = 70,default="NA")
   pincode = models.IntegerField(default=000000)
   status=models.CharField(max_length = 100,default="NA")
   link=models.URLField(max_length = 200,default="http://")
   verified = models.BooleanField(default=False)
   
   class Meta:
      db_table = "Ambulance"

class BloodPlasma(models.Model):

   name = models.CharField(max_length = 50)
   contact_number = models.IntegerField()
   contact_person = models.CharField(max_length =100,default="NA")
   address = models.CharField(max_length = 70,default="NA")
   link=models.URLField(max_length = 200,default="http://")
   medical_conditions = models.CharField(max_length = 70,default="NA")
   availibility_status= models.CharField(max_length = 100,default="NA")
   verified = models.BooleanField(default=False)
   
   class Meta:
      db_table = "Bloodplasma"

class Medicine(models.Model):

   name = models.CharField(max_length = 50, default="NA")
   pharmacy = models.CharField(max_length=100, default="NA")
   contact_number = models.IntegerField()
   status = models.CharField(max_length =100,default="NA")
   last_verified = models.DateTimeField()

   
   class Meta:
      db_table = "Medicine"

class EConsultation(models.Model):

   name = models.CharField(max_length = 50, default="NA")
   contact_number = models.IntegerField()
   area = models.CharField(max_length=200, default="NA")
   contact_person = models.CharField(max_length=100, default="NA")
   status = models.CharField(max_length = 200, default="NA")
   last_verified = models.DateTimeField()
   
   class Meta:
      db_table = "Econsultation"

class Patient(models.Model):

   name = models.CharField(max_length = 50)
   age = models.IntegerField()
   contact_number = models.IntegerField()
   contact_person = models.CharField(max_length =100,default="NA")
   hospital_admission_status = models.BooleanField()
   hospital_name = models.CharField(max_length = 50)
   doctor_name = models.CharField(max_length = 50)
   doctor_contactnum = models.IntegerField()
   requirement = models.CharField(max_length = 50)
   caretaker_number = models.IntegerField()
   verified = models.BooleanField(default=False)
   
   class Meta:
      db_table = "Patient"

class PlasmaXchange(models.Model):
   PatientName = models.CharField(max_length=50)
   PatientAge = models.IntegerField()
   PatientBloodGroup = models.CharField(max_length=3)
   PatientContact = models.IntegerField()
   PatientAddress = models.CharField(max_length=200)
   # donor fiels
   DonorName = models.CharField(max_length=50)
   DonorAge = models.IntegerField()
   DonorBloodGroup = models.CharField(max_length=3)
   DonorContact = models.IntegerField()
   DonorAddress = models.CharField(max_length=200)

   class Meta:
      db_table = "Plasmaxchange"


class RequestedResource(models.Model):
   available_resources =[
      ('Oxygen', 'Oxygen'),
    ('Bloodplasma', 'Bloodplasma'),
    ('Foodsupport', 'Foodsupport'),
    ('Econsultation', 'Econsultation'),
    ('Medicine', 'Medicine'),
   ]

   cho_status=[
      ('Pending', 'Pending'),
      ('Ok','Ok'),
      ('Failed', 'Failed'),
   ]

   user=models.ForeignKey(User, on_delete=models.DO_NOTHING,default=None,null=True)
   resource = models.CharField(choices=available_resources,max_length=50)
   status=models.CharField(choices=cho_status,default="Pending",max_length=50)

   class Meta:
      db_table = "RequestedResource"
   def __str__(self):
      print(self.user)
      return self.resource+" Requested By "+self.user.username
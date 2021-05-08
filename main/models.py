from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    pass


class Oxygen(models.Model):

   name = models.CharField(max_length = 50)
   contact_number = models.IntegerField()
   contact_person = models.IntegerField()
   website = models.URLField(max_length = 200)
   status = models.CharField(max_length = 50)
   last_verified=  models.DateField()
   address = models.CharField(max_length = 70)
   
   class Meta:
      db_table = "Oxygen"

class FoodSupport(models.Model):

   name = models.CharField(max_length = 50)
   contact_number = models.IntegerField()
   address = models.CharField(max_length = 70)
   no_of_meals = models.IntegerField()
   verified = models.BooleanField()

   class Meta:
      db_table = "FoodSupport"

class Ambulance(models.Model):

   name = models.CharField(max_length = 50)
   contact_number = models.IntegerField()
   contact_person = models.IntegerField()
   address = models.CharField(max_length = 70)
   pincode = models.IntegerField()
   verified = models.BooleanField()
   
   class Meta:
      db_table = "Ambulance"

class BloodPlasma(models.Model):

   name = models.CharField(max_length = 50)
   contact_number = models.IntegerField()
   blood_group = models.CharField(max_length = 4)
   address = models.CharField(max_length = 70)
   medical_conditions = models.CharField(max_length = 70)
   required_bloodgroup = models.CharField(max_length = 4)
   verified = models.BooleanField()
   
   class Meta:
      db_table = "BloodPlasma"

class Medicine(models.Model):

   name = models.CharField(max_length = 50)
   contact_number = models.IntegerField()
   quantity = models.IntegerField()
   expiry_date=  models.DateField()
   verified = models.BooleanField()
   
   class Meta:
      db_table = "Medicine"

class EConsultation(models.Model):

   name = models.CharField(max_length = 50)
   contact_number = models.IntegerField()
   link = models.URLField(max_length = 200)
   verified = models.BooleanField()
   
   class Meta:
      db_table = "EConsultation"

class Patient(models.Model):

   name = models.CharField(max_length = 50)
   age = models.IntegerField()
   contact_number = models.IntegerField()
   hospital_admission_status = models.BooleanField()
   hospital_name = models.CharField(max_length = 50)
   doctor_name = models.CharField(max_length = 50)
   doctor_contactnum = models.IntegerField()
   requirement = models.CharField(max_length = 50)
   caretaker_number = models.IntegerField()
   verified = models.BooleanField()
   
   class Meta:
      db_table = "Patient"
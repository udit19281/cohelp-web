from django.contrib import admin
from main.models import *
# Register your models here.

admin.site.register([User,Oxygen,FoodSupport,
Ambulance, BloodPlasma, Medicine, EConsultation,
Patient])

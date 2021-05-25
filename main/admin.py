from django.contrib import admin
from main.models import *
# Register your models here.

admin.site.register([User,PlasmaXchange,RequestedResource])
admin.site.register([ResourceTable,AddResource])

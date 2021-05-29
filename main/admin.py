from django.contrib import admin
from main.models import *
# Register your models here.

admin.site.site_header = 'Administration Tool'

class resourcetable(admin.ModelAdmin):
    list_display=[field.name for field in ResourceTable._meta.get_fields()]
    list_filter=[field.name for field in ResourceTable._meta.get_fields()]
    pass

class reqtable(admin.ModelAdmin):
    list_display=[field.name for field in RequestedResource._meta.get_fields()]
    list_filter=[field.name for field in RequestedResource._meta.get_fields()]
    
    pass
class plastable(admin.ModelAdmin):
    list_display=[field.name for field in PlasmaXchange._meta.get_fields()]
    list_filter=['username','id','status']
    pass
admin.site.register(Profile)
admin.site.register(PlasmaXchange,plastable)
admin.site.register(RequestedResource,reqtable)
admin.site.register(ResourceTable,resourcetable)
admin.site.register(AddResource)
admin.site.register(VolunteerRequest)

from django.contrib import admin
from .models.health_care import *
from .models.contact import *
from .models.appointment import *


#=============================== Health =================================================

class AdminHealth(admin.ModelAdmin):
    list_display = ['id','center','state','city','pincode']
#=========================================================================================



#================================ Contact =================================================
class AdminContact(admin.ModelAdmin):
    list_display = ['id','name','email','subject','message']

#============================================================================================
#============================================================================================



#================================ Appointment ===============================================
class AdminAppointment(admin.ModelAdmin):
    list_display = ['id','name','number','service','doctor','date','time']

#===========================================================================================
#============================================================================================



#===================================== Register =============================================
admin.site.register(Health, AdminHealth)
admin.site.register(Contact, AdminContact)
admin.site.register(Appointment, AdminAppointment)
#============================================================================================
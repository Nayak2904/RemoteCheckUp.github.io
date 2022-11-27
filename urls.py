from django.contrib import admin
from django.conf.urls.static import static
from . import settings
from django.urls import path
from hospital.main_views import *


#======================================Urls =================================================

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', index,name='index'),
    path('',Login.as_view(),name='login'),
    path('signup',Signup.as_view(),name='signup'),
    path('dologout',dologout,name='dologout'),
    path('contact',contact,name='contact'),
    path('report',report,name='report'),
    path('book_appointment',book_appointment,name='book_appointment'),
    path('appointment',appointment,name='appointment'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#============================================================================================
#============================================================================================
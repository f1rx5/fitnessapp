from django.urls import path,include
from . import views
urlpatterns=[
    path('master/',views.fnmaster,name='master'),
    path('home/', views.fnhome, name='home'),
    path('about/',views.fnabout,name='about'),
    path('classes/',views.fnclasses,name='classes'),
    path('register/',views.fnregister,name='register'),
    path('master2/',views.fnmaster2,name='master2'),
    path('user/',views.fnuser,name='user'),
    path('usermaster/',views.fnmaster3,name='usermaster'),
    path('viewworkout/',views.fnworkout,name='viewworkout'),
    path('viewdiet/',views.fndiet,name='viewdiet'),
    path('contact/',views.fncontact,name='contact'),
]
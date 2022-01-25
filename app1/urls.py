from django.urls import path,include
from . import views
urlpatterns=[
    path('master/',views.fnmaster,name='master'),
    path('home/', views.fnhome, name='home'),
    path('about/',views.fnabout,name='about'),
    path('classes/',views.fnclasses,name='classes'),
    path('register/',views.fnregister,name='register'),
]
from django.urls import path,include
from . import views
urlpatterns=[
    path('login/',views.fnlogin,name='login'),
    path('adminmaster/',views.fnmaster,name='masteradmin'),
    path('admindash/',views.fndash,name='admindashboard'),
    path('adminuser/',views.fnuser,name='adminuser'),
    path('admintrainers/',views.fntrainers,name='admintrainers'),
    path('viewreview/',views.fnreview,name='viewreview'),
    path('addtrainers/',views.fnaddtrainers,name='addtrainers')
]
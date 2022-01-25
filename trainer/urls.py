from nturl2path import url2pathname
from django.urls import URLPattern, path,include
from . import views
urlpatterns=[
    path('trainermaster/',views.fntrainermaster,name='trainermaster'),
    path('trainerclient/',views.fnclient,name='trainerclient'),
]
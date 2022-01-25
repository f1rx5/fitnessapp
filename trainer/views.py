from django.shortcuts import render

# Create your views here.
def fntrainermaster(request):
    return render(request,'trainermaster.html')
def fnclient(request):
    return render(request,'trainerclient.html')

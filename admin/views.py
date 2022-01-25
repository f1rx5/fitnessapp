from django.shortcuts import render

# Create your views here.
def fnlogin(request):
    return render(request,'adminlogin.html')
def fnmaster(request):
    return render(request,'adminmaster.html')
def fndash(request):
    return render(request,'admindashboard.html')
def fnuser(request):
    return render(request,'adminuser.html')
def fntrainers(request):
    return render(request,'admintrainers.html')
def fnreview(request):
    return render(request,'viewreviews.html')
def fnaddtrainers(request):
    return render(request,'addtrainers.html')
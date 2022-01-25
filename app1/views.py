from django.shortcuts import render

# Create your views here.
def fnhome(request):
    return render(request,'home.html')
def fnmaster(request):
    return render(request,'masters.html')
def fnabout(request):
    return render(request,'aboutus.html')
def fnclasses(request):
    return render(request,'classes.html')
def fnregister(request):
    return render(request,'register.html')
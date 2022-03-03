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
def fnmaster2(request):
    return render(request,'master2.html')
def fnuser(request):
    return render(request,'userprofile.html')
def fnmaster3(request):
    return render(request,'usermaster.html')
def fnworkout(request):
    return render(request,'viewworkout.html')
def fndiet(request):
    return render(request,'viewdiet.html')
def fncontact(request):
    return render(request,'contact.html')


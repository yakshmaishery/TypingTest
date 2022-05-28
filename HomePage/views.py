from django.shortcuts import render,HttpResponse
import random

# Create your views here.
def home(request):
    return render(request,"Home.html")
    
def SimpleTest(request):
    
    return render(request,"SimpleTest.html")
    
def MediumPage(request):
    return render(request,"MediumTest.html")
    
def HardPage(request):
    return render(request,"HardTest.html")
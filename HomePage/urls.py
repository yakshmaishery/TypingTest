from django.contrib import admin
from django.urls import path
from HomePage import views

urlpatterns = [
    path("",views.home,name="Home Page"),
    path("SimpleTest",views.SimpleTest,name="Test Page"),
    path("MediumPage",views.MediumPage,name="Test Page"),
    path("HardPage",views.HardPage,name="Test Page"),
]

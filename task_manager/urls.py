from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def home(request):
    return HttpResponse("Приветствие!")

urlpatterns = [
    path("", home, name="home"),
    path("", home),
]
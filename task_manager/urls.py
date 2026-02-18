from django.urls import path
from django.http import HttpResponse

def home(request):
    return HttpResponse("Приветствие!")

urlpatterns = [
    path("", home),
]
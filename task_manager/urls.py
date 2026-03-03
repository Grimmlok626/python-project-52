from django.urls import path
from django.shortcuts import render
from . import views

def home(request):
    return render(request, "home.html")

urlpatterns = [
    path('', home, name='home'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('register/', views.register, name='register'),
    path('users/', views.users_list, name='users'),
]
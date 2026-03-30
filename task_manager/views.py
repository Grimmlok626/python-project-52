from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.models import User
from task_manager.users.forms import RegisterForm
from django.shortcuts import render

def home(request):
    return render(request, "home.html")
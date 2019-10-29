from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
# Create your views here.


def login(request):
    return render(request, 'login.html')


def mess(request):
    return render(request, 'mess.html')
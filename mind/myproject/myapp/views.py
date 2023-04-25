from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def HomePage(request):
    return render(request, 'home.html')



def SignIn(request):
    return render(request, 'signin.html')


def TakeTest(request):
    return render(request, 'taketest.html')



# Create your views here.


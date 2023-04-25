from django.shortcuts import render, HttpResponse, redirect
from .models import user_id
from django.contrib.auth import authenticate, login, logout
from .forms import CRUDFORM

def HomePage(request):
    return render(request, 'home.html')



def SignIn(request):
    return render(request, 'signin.html')


def TakeTest(request):
    return render(request, 'taketest.html')

def SignUp (request):
    form = CRUDFORM(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect ('taketest.html')
    context = {
        "form":form
    }
    return render(request, 'signup.html', context)

# Create your views here.


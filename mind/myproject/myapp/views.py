from django.shortcuts import render, HttpResponse, redirect
from .models import user_id
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import CRUDFORM
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
# from myapp.backends import EmailBackend
from .authentication import EmailBackend

import pdb
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import QuizResponse
from .serializers import QuizResponseSerializer



def HomePage(request):
    return render(request, 'home.html')

def SignIn(request):
    print(request.method)
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email, password)
        user = EmailBackend().authenticate(request=request, email=email, password=password, model=user_id, backend='myapp.backends.EmailBackend' )
        print("user is ",user)
        if user:
            request.session['user'] = str(user).upper()
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials. Please try again.')
            return render(request, 'signin.html')
    return render(request, 'signin.html')


def TakeTest(request):
    return render(request, 'taketest.html')

def SignUp (request):
    form = CRUDFORM(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect ('taketest')
    context = {
        "form":form
    }
    return render(request, 'signup.html', context)



class QuizResponseView(APIView):
    def post(self, request):
        serializer = QuizResponseSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Data received successfully'}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

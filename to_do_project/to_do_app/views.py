from logging import log
import re
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.messages import constants as messages
# Create your views here.

def index(request):
    return render(request,'to_do_app/index.html')

def user_signup(request):
    if request.method == 'GET':
        return render(request, 'to_do_app/user_signup.html', {'form':UserCreationForm()})
    else:
        #Check if initial password and confirmation password match
        if request.POST['password1'] == request.POST['password2']:
            #The Post Request(AKA Signing up and creating the User model.)
            try:
                user = User.objects.create_user(request.POST['username'], password = request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('current_todos')
            except IntegrityError:
                return render(request,'to_do_app/user_signup.html',{'form':UserCreationForm(), 'error':'User name is already taken.'})
        else:
            return render(request,'to_do_app/user_signup.html',{'form':UserCreationForm(), 'error':'Passwords do not match'})

def current_todos(request):
        return render(request,'to_do_app/current_todos.html')

def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index')
        # messages.info(request, "Logged out successfully!")

def login_user(request):
    if request.method == 'GET':
        return render(request, 'to_do_app/login_user.html', {'form':AuthenticationForm()})
    else:
    #Check if initial password and confirmation password match
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'to_do_app/login_user.html', {'form':AuthenticationForm(),
            'error':'INVALID CREDNTIALS'})
        else:
            login(request,user)
            return redirect('current_todos')

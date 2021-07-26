from logging import log
import re
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
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
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('index')
    else:
        pass
        # Return an 'invalid login' error message.
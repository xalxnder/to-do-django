from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
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
                return render(request,'to_do_app/user_signup.html',{'form':UserCreationForm(), 'success':'User added!'})
            except IntegrityError:
                return render(request,'to_do_app/user_signup.html',{'form':UserCreationForm(), 'error':'User name is already taken.'})
        else:
            return render(request,'to_do_app/user_signup.html',{'form':UserCreationForm(), 'error':'Passwords do not match'})

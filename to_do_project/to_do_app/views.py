from django.shortcuts import render

# Create your views here.
def user_signup(request):
    return render(request, 'to_do_app/user_signup.html')
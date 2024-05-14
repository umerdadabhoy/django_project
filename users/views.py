from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.hashers import make_password , check_password
from django.contrib.auth import login , authenticate , logout
from .models import User


#function to check whether user is logged in or not
def check_login(function):

    def check(request,*args, **kwargs):

        if str(request.user) == "AnonymousUser": 
            return user_register(request)
        else:
            return function(request)

    return check

# Create your views here.
def user_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        User.objects.create(username=username,email=email,password= make_password(password))

    return render(request, 'users/user_register.html')


def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        #email_status = User.objects.filter(email=email).exists()
        #system_password = User.objects.filter(email=email).values_list("password")[0][0]
        #password_status = check_password(password,system_password)
        user = authenticate(request , email=email,password=password)
        if user is not None:
            login(request, user)
            return redirect('app1.index')
        #print(email_status , password_status)
    return render(request , 'users/user_login.html')


#logout user
def user_logout(request):
    logout(request)
    return redirect('users.register')
#check email at signup screen for existance
def check_email(request, *args, **kwargs):
    if request.method == 'POST':
        email1 = request.POST.get('email')
        status = User.objects.filter(email = email1).exists()
        if status:
            return HttpResponse(status)
        else:
            return HttpResponse(status)
        #
    #return redirect('users.register')
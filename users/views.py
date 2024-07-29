from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse='login')
    else:
        return render(request, 'users/index.html', {'user': request.user})


def login_view(request):
    if request.method =="POST":
        username_or_email = request.POST["username_or_email"]
        password =request.POST["password"]
        user= authenticate(request,username=username_or_email,password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse('users:index'))
        else:
            return render(request,'users/login.html',{
                "error_message":'Invalid credentials'
            })
    return render(request,'users/login.html')

def logout_view(request):
    logout(request)
    return render(request,'users/login.html',{
        "message":'logged out'
    })

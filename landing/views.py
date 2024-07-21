from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,"statue/index.html")

def available(request):
    return HttpResponse("List of things that are available.")

def greet(request,name):
    return render(request,'statue/greet.html',{
        'name':name.capitalize(),
    })
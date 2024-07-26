from django.shortcuts import render
from .models import Flight,Airport
# Create your views here.
def index(request):
    return render(request,"flight/index.html",{
        "flight":Flight.objects.all()
    })
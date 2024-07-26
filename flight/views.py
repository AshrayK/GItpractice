from django.shortcuts import render
from .models import Flight,Passenger
# Create your views here.

def index(request):
    return render(request,"flight/index.html",{
        "flight":Flight.objects.all()
    })

def flight(request,flight_id):
    flight=Flight.objects.get(id=flight_id)
    return render(request,"flight/flight.html",{
        "flight":flight,
        "passengers":flight.passengers.all(),
    })
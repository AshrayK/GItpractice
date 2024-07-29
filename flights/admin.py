from django.contrib import admin
from .models import Flight, Airport, Passenger


class FlightAdmin(admin.ModelAdmin):
    list_display=('id','origin','destination','duration')
    list_filter = ('origin','destination')
    ordering = ('id','origin','destination','duration')

class AirportAdmin(admin.ModelAdmin):
    list_display=('id','city','code')
    list_filter = ('city','code')
    ordering = ('id','city','code')

class PassengerAdmin(admin.ModelAdmin):
    list_display = ('id','first','last')
    list_filter = ('first','last')
    ordering = ('id','first','last')
    filter_horizontal = ('flights',)


# Register your models here.
admin.site.register(Flight,FlightAdmin)
admin.site.register(Airport,AirportAdmin)
admin.site.register(Passenger,PassengerAdmin)
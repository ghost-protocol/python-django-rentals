from django.contrib import admin
from .models import Cartype, Car, Location, Order, Client

# Register your models here.
admin.site.register(Cartype)
admin.site.register(Car)
admin.site.register(Location)
admin.site.register(Order)
admin.site.register(Client)

from django.contrib import admin
from .models import Car, Gassing, Detailer

# Register your models here.
admin.site.register(Car)
admin.site.register(Gassing)
admin.site.register(Detailer)

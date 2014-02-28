from django.contrib import admin

from .models import Weatherstation, Weatherdata


# Register your models here.
admin.site.register(Weatherdata)
admin.site.register(Weatherstation)

from django.contrib import admin

from .models import Weatherstation, Weatherdata, Cities, Countries


# Register your models here.
admin.site.register(Weatherdata)
admin.site.register(Weatherstation)
admin.site.register(Cities)
admin.site.register(Countries)

from django.contrib.gis import admin

from .models import Stay

# Register your models here.

admin.site.register(Stay, admin.GeoModelAdmin)
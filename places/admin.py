from django.contrib.gis import admin

from .models import Place

# Register your models here.

admin.site.register(Place, admin.GeoModelAdmin)
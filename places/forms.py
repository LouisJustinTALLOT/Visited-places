from django.contrib.gis import forms
from django.contrib.gis.db import models as gis_models
from django.contrib.gis.forms import ModelForm

from .models import Place

# class PlaceForm(forms.Form):
#     name = forms.CharField(label="Nom du lieu")
#     date_visited = forms.DateField(label="Date de dernière visite")

#     # coordinates = gis_models.PointField(verbose_name="Coordonnées", geography=True)
#     coordinates = gis_models.PointField(verbose_name="Coordonnées", geography=True, widget= forms.OSMWidget(attrs={'map_width': 800, 'map_height': 500}))

class PlaceForm(forms.ModelForm):
    
    class Meta:
        model = Place
        fields = ("name","date_visited", "coordinates",)

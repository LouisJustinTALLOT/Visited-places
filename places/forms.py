from django.contrib.gis import forms
import floppyforms.__future__ as floppyforms

from django.contrib.gis.db import models as gis_models
from django.contrib.gis.forms import ModelForm

from .models import Stay


class MultiPointWidget(floppyforms.gis.MultiPointWidget, floppyforms.gis.BaseOsmWidget):
    pass

class PointWidget(floppyforms.gis.PointWidget, floppyforms.gis.BaseOsmWidget):
    pass

class PlaceForm(floppyforms.ModelForm):
    class Meta:
        model = Stay
        fields = ("name","date_visited", "coordinates", "visits",)
        widgets = {
            "name": floppyforms.TextInput(attrs={"placeholder": "Nom du lieu"}),
            "date_visited": floppyforms.DateInput(attrs={"type": "date"}),
            "coordinates": PointWidget(),
            "visits": MultiPointWidget(),
        }

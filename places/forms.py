from django.contrib.gis import forms

class PlaceForm(forms.Form):
    name = forms.CharField(label="Nom du lieu")
    date_visited = forms.DateField(label="Date de dernière visite")

    # coordinates = forms.PointField(label="Coordonnées")
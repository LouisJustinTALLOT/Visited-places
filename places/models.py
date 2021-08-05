from django.db import models
from django.contrib.gis.db import models as gis_models

# Create your models here.
class Place(models.Model):
    """Model storing a location that has been visited"""

    name = models.TextField(verbose_name="Nom du lieu")
    date_visited = models.DateField(verbose_name="Date de dernière visite")

    coordinates = gis_models.PointField(verbose_name="Coordonnées", null=True, blank=True)
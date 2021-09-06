from django.db import models
from django.contrib.gis.db import models as gis_models

# Create your models here.
class Stay(models.Model):
    """Model storing a place that has been travelled to"""

    name = models.TextField(verbose_name="Lieu du voyage")
    date_visited = models.DateField(verbose_name="Date de dernière visite")

    coordinates = gis_models.PointField(verbose_name="Coordonnées", null=True, blank=True)

    class Meta:
        verbose_name = "Voyage"
        verbose_name_plural = "Voyages"
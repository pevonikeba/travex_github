from django.db import models
from django.contrib.gis.db import models as gis_models
from loguru import logger

from place.models import Place, CustomUser

CONTINENT_CHOICES =(
    ("Asia", "Asia"),
    ("Africa", "Africa"),
    ("Europe", "Europe"),
    ("North America", "North America"),
    ("South America", "South America"),
    ("Australia/Oceania", "Australia/Oceania"),
    ("Antarctica", "Antarctica"),
)


class Location(models.Model):
    # place = models.OneToOneField(Place, related_name="locations", on_delete=models.CASCADE, primary_key=True)
    # continent = models.CharField(choices=CONTINENT_CHOICES, max_length=20, default="Asia")
    location_id = models.IntegerField(null=True, blank=True)
    point = gis_models.PointField(srid=4326, null=True, blank=True)
    latitude = models.DecimalField(max_digits=13, decimal_places=10, null=True, blank=True)
    longitude = models.DecimalField(max_digits=13, decimal_places=10, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    country_code = models.CharField(max_length=5, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    county = models.CharField(max_length=255, null=True, blank=True)
    region = models.CharField(max_length=255, null=True, blank=True)
    subregion = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    town = models.CharField(max_length=255, null=True, blank=True)
    district = models.CharField(max_length=255, null=True, blank=True)
    subdistrict = models.CharField(max_length=255, null=True, blank=True)
    municipality = models.CharField(max_length=255, null=True, blank=True)
    iso_3166_2_lvl4 = models.CharField(max_length=20, null=True, blank=True)
    postal_code = models.CharField(max_length=15, null=True, blank=True)
    road = models.CharField(max_length=255, null=True, blank=True)
    house_number = models.CharField(max_length=10, null=True, blank=True)

    class Meta:
        abstract = True

    # def save(self, *args, **kwargs):
    #     if self.latitude and self.longitude:
    #         logger.info("da")
    #     return super(Location, self).save(args, kwargs)

class PlaceLocation(Location):
    place = models.OneToOneField(Place, related_name="location", on_delete=models.CASCADE, primary_key=True)

    # def __str__(self):
    #     return f"Location of {self.place}"


class UserLocation(Location):
    writer_user = models.OneToOneField(CustomUser, related_name="location", on_delete=models.CASCADE, primary_key=True)

    # def __str__(self):
    #     return f"Location of {self.writer_user}"



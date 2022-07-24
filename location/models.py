from django.contrib.gis.geos import Point
from django.db import models
from django.contrib.gis.db import models as gis_models
from loguru import logger

from location.config import geopy_response, service_to_location_data, place_names, additional_place_names
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

# from django.db.models import Q


class BaseLocation(models.Model):
    name = models.CharField(null=True, blank=True, max_length=255)
    point = gis_models.PointField(srid=4326, null=True, blank=True)
    latitude = models.DecimalField(max_digits=25, decimal_places=20, null=True, blank=True)
    longitude = models.DecimalField(max_digits=25, decimal_places=20, null=True, blank=True)

    class Meta:
        abstract = True


class HasLocationManager(models.Manager):
    def get_queryset(self):
        # return super().get_queryset().exclude(Q(latitude__isnull=True) | Q(longitude__isnull=True))
        return super().get_queryset().exclude(point__isnull=True)


class ChooseLocation(BaseLocation):
    DISTRICT = 'District'
    CITY = 'City'
    SUBREGION = 'Subregion'
    REGION = 'Region'
    CHOOSE_LOCATION_CHOICES = (
        (DISTRICT, 'District'),
        (CITY, 'City'),
        (SUBREGION, 'Subregion'),
        (REGION, 'Region'),
    )
    type = models.CharField(max_length=12, choices=CHOOSE_LOCATION_CHOICES)
    country_name = models.CharField(max_length=255)
    objects = models.Manager()  # The default manager.
    has_locations = HasLocationManager()

    def __str__(self):
        return f'{self.type}: {self.name} ({self.country_name})'

    def save(self, *args, **kwargs):
        if self.latitude and self.longitude:
            self.point = Point(float(self.longitude), float(self.latitude), srid=4326)
        return super(ChooseLocation, self).save(args, kwargs)


class ServiceLocation(models.Model):
    location_id = models.IntegerField(null=True, blank=True)
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

    def data_to_field(self, data):
        self.point = data.get('point')
        self.location_id = data.get('location_id')
        self.country = data.get('country')
        self.country_code = data.get('country_code')
        self.state = data.get('state')
        self.county = data.get('county')
        self.city = data.get('city')
        self.subregion = data.get('subregion')
        self.region = data.get('region')
        self.town = data.get('town')
        self.district = data.get('district')
        self.subdistrict = data.get('subdistrict')
        self.municipality = data.get('municipality')
        self.iso_3166_2_lvl4 = data.get('iso_3166_2_lvl4')
        self.postal_code = data.get('postal_code')
        self.road = data.get('road')
        self.house_number = data.get('house_number')


class PlaceLocation(BaseLocation, ServiceLocation):
    place = models.OneToOneField(Place, related_name="location", on_delete=models.CASCADE, primary_key=True)
    
    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.longitude and self.latitude:
            data = service_to_location_data({'longitude': self.longitude, 'latitude': self.latitude})
            self.data_to_field(data)
            logger.info(data)
            self.name = data.get('name')

        return super(PlaceLocation, self).save(force_insert, force_update, using, update_fields)


class UserLocation(BaseLocation, ServiceLocation):
    writer_user = models.OneToOneField(CustomUser, related_name="location", on_delete=models.CASCADE, primary_key=True)
    HOME = 'hm'
    WORK = 'wk'
    OTHER = 'ot'
    PLACE_TYPE_CHOICES = (
        (HOME, 'Home'),
        (WORK, 'Work'),
        (OTHER, 'Other'),
    )
    place_type = models.CharField(max_length=2, choices=PLACE_TYPE_CHOICES, null=True, blank=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.longitude and self.latitude:
            data = service_to_location_data({'longitude': self.longitude, 'latitude': self.latitude})
            self.data_to_field(data)
            self.name = data.get('name')

        return super(UserLocation, self).save(force_insert, force_update, using, update_fields)

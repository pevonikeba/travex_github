from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point
from loguru import logger
from rest_framework import viewsets, mixins, filters
from cities.models import City, District, Country, PostalCode

from location.serializers import CitySerializer, DistrictSerializer, CountrySerializer, PostalCodeSerializer


class CityViewSet(mixins.ListModelMixin,
                      viewsets.GenericViewSet):
    # queryset = City.objects.all()
    serializer_class = CitySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', ]

    def get_queryset(self):
        # london = City.objects.filter(country__name='United Kingdom').get(name='London')
        # # nearest = City.objects.distance(london.location).exclude(id=london.id).order_by('distance')[:5]
        # nearest = City.objects.annotate(
        #     distance=Distance('location', london.location)
        # ).exclude(id=london.id).order_by('distance')[:5]
        # logger.debug(nearest)
        queryset = City.objects.all()
        long = self.request.query_params.get('long')
        lat = self.request.query_params.get('lat')
        if long is not None and lat is not None:
            requested_place = Point(float(long), float(lat), srid=4326)
            logger.info(requested_place)
            queryset = queryset.annotate(
                distance=Distance('location', requested_place)
                ).order_by('distance')

        return queryset


class DistrictViewSet(mixins.ListModelMixin,
                      viewsets.GenericViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', ]


class CountryViewSet(mixins.ListModelMixin,
                     viewsets.GenericViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', ]


class PostalCodeViewSet(mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    queryset = PostalCode.objects.all()
    serializer_class = PostalCodeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['code', ]

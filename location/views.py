from itertools import chain

from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point
from drf_multiple_model.pagination import MultipleModelLimitOffsetPagination
from drf_multiple_model.views import ObjectMultipleModelAPIView, FlatMultipleModelAPIView
from drf_multiple_model.viewsets import FlatMultipleModelAPIViewSet
from geopy import Nominatim
from loguru import logger
from rest_framework import viewsets, mixins, filters
from rest_framework.response import Response
from rest_framework.views import APIView

from cities.models import City, District, Country, PostalCode, Region, Subregion

from location.serializers import CitySerializer, DistrictSerializer, CountrySerializer, PostalCodeSerializer, \
    LocationSerializer


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


class LocationViewSet(mixins.ListModelMixin,
                      viewsets.GenericViewSet):
    serializer_class = LocationSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', ]

    def get_queryset(self):
        # queryset = City.objects.all().values_list(
        #     'name', 'location'
        # ).union(
        #     District.objects.all().values_list(
        #         'name', 'location'
        #     )
        # )
        # long = self.request.query_params.get('long')
        # lat = self.request.query_params.get('lat')
        # if long is not None and lat is not None:
        #     requested_place = Point(float(long), float(lat), srid=4326)
        #     logger.info(requested_place)
        #     queryset = queryset.annotate(
        #         distance=Distance('location', requested_place)
        #         ).order_by('distance')
        queryset = City.objects.all()
        queryset1 = District.objects.all()
        return chain(queryset, queryset1)


class LimitPagination(MultipleModelLimitOffsetPagination):
    default_limit = 2


class HomeAPIView(FlatMultipleModelAPIView):
    # permission_classes = (Isa,)
    querylist = [
        {'queryset': City.objects.all(), 'serializer_class': LocationSerializer},
        {'queryset': District.objects.all(), 'serializer_class': LocationSerializer},
    ]
    pagination_class = LimitPagination


def has_location_filtered_queryset(model, longitude: str, latitude: str):
    if longitude and latitude:
        requested_point = Point(float(longitude), float(latitude), srid=4326)
        queryset = model.objects.annotate(
            distance=Distance('location', requested_point)
        ).order_by('distance')

    return queryset


from django.db.models import OuterRef, Subquery


def not_2_has_location_filtered_queryset(model, longitude: str, latitude: str):
    requested_point = Point(float(longitude), float(latitude), srid=4326)
    cities = City.objects.filter(region=OuterRef('pk'))
    region_queryset = Region.objects.annotate(location=Subquery(cities.values('location')[:1]))

    queryset = Subregion.objects.annotate(location=Subquery(cities.values('location')[:1])).annotate(
        distance=Distance('location', requested_point)
    ).order_by('distance')

    return queryset


def not_has_location_filtered_queryset(model, longitude: str, latitude: str):
    requested_point = Point(float(longitude), float(latitude), srid=4326)
    cities = City.objects.filter(region=OuterRef('pk'))
    queryset = model.objects.annotate(location=Subquery(cities.values('location')[:1])).annotate(
        distance=Distance('location', requested_point)
    ).order_by('distance')

    return queryset


class ChooseViewSet(FlatMultipleModelAPIViewSet):
    pagination_class = LimitPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', ]

    def get_querylist(self):
        longitude = self.request.query_params.get('longitude')
        latitude = self.request.query_params.get('latitude')

        district_queryset = has_location_filtered_queryset(District,
                                                           longitude,
                                                           latitude)
        city_queryset = has_location_filtered_queryset(City,
                                                       longitude,
                                                       latitude)
        subregion_queryset = not_has_location_filtered_queryset(Subregion,
                                                                longitude,
                                                                latitude)
        region_queryset = not_has_location_filtered_queryset(Region,
                                                             longitude,
                                                             latitude)

        # title = self.request.query_params['play'].replace('-', ' ')

        querylist = [
            {'queryset': district_queryset, 'serializer_class': LocationSerializer},
            {'queryset': city_queryset, 'serializer_class': LocationSerializer},
            {'queryset': subregion_queryset, 'serializer_class': LocationSerializer},
            {'queryset': region_queryset, 'serializer_class': LocationSerializer},
        ]

        # querylist = (
        #     {'queryset': Play.objects.filter(title=title), 'serializer_class': PlaySerializer},
        #     {'queryset': Poem.objects.filter(style="Sonnet"), 'serializer_class': PoemSerializer},
        # )

        return querylist

import requests

def get_location(lat, lon):
    url = f'https://nominatim.openstreetmap.org/reverse?lat={lat}&lon={lon}&format=json&accept-language=en&zoom=10'
    try:
        result = requests.get(url=url)
        result_json = result.json()
        logger.warning(result_json)
        return result_json
    except:
        return None


class DetectView(APIView):
    def get(self, request, format=None):
        latitude = 37.9303
        longitude = 58.369
        get_location(latitude, longitude)

        geolocator = Nominatim(user_agent="travel-attaplace")
        coordinate = f"{longitude}, {latitude}"
        location = geolocator.reverse(coordinate)
        logger.info(location.address.country)
        print(location.address, "\n")
        return Response(location.address)
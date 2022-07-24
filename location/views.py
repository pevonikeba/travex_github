from itertools import chain

from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point
from drf_multiple_model.pagination import MultipleModelLimitOffsetPagination
from drf_multiple_model.views import ObjectMultipleModelAPIView, FlatMultipleModelAPIView
from drf_multiple_model.viewsets import FlatMultipleModelAPIViewSet
from geopy import Nominatim
# from OSMPythonTools.nominatim import Nominatim as OSMPythonToolsNominatim

from loguru import logger
from rest_framework import viewsets, mixins, filters, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from cities.models import City, District, Country, PostalCode, Region, Subregion
from location.config import geopy_response
from location.models import PlaceLocation, UserLocation, ChooseLocation

from location.serializers import CitySerializer, DistrictSerializer, CountrySerializer, PostalCodeSerializer, \
    LocationSerializer, PlaceLocationSerializer, UserLocationSerializer
from place.models import Place
from place.serializers.place.list import PlaceListSerializer


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
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['code', ]


class LocationViewSet(mixins.ListModelMixin,
                      viewsets.GenericViewSet):
    serializer_class = LocationSerializer
    permission_classes = [IsAuthenticated]
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
    permission_classes = (IsAuthenticated)
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


from django.db.models import OuterRef, Subquery, Q


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


class ChooseViewSet(mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', ]

    def get_queryset(self):
        longitude = self.request.query_params.get('longitude')
        latitude = self.request.query_params.get('latitude')
        requested_point = Point(float(longitude), float(latitude), srid=4326)

        return ChooseLocation.has_locations.all()


class ChooseViewSetOld(FlatMultipleModelAPIViewSet):
    pagination_class = LimitPagination
    permission_classes = [IsAuthenticated]
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
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        longitude = request.query_params.get('longitude')
        latitude = request.query_params.get('latitude')
        # location by url
        # location_by_url = get_location(latitude, longitude)
        # location by nominatim (detailed than url: for ex. has house number)

        response = geopy_response(latitude, longitude)

        # logger.info(response)
        return Response(response)


geolocator = Nominatim(user_agent="geoapiExercises")


def city_state_country(coord):
    location = geolocator.reverse(coord, exactly_one=True, language='en')
    address = location.raw['address']
    city = address.get('city', '')
    state = address.get('state', '')
    country = address.get('country', '')
    return city, state, country


class PlaceLocationViewSet(viewsets.ModelViewSet):
    queryset = PlaceLocation.objects.all()
    serializer_class = PlaceLocationSerializer
    permission_classes = [IsAuthenticated]

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #
    #     if serializer.is_valid():
    #         latitude = serializer.validated_data.get("latitude")
    #         longitude = serializer.validated_data.get('longitude')
    #         if latitude and longitude:
    #             logger.error(city_state_country(f"{latitude}, {longitude}"))
    #             location = get_location(latitude, longitude)
    #             if not location:
    #                 raise ValueError('Can\'t connect to nominatim server')
    #             logger.info('goood')
    #             logger.info(location)
    #             address = location.get("address")
    #             logger.warning(address)
    #             # extra_data = serializer.data
    #             if address:
    #                 country = address.get("country")
    #                 state = address.get("state")
    #                 county = address.get("county")
    #                 city = address.get("city")
    #                 # TODO: get continent
    #                 serializer.save(country=country,
    #                                 city=city,
    #                                 state=state,
    #                                 county=county,
    #                                 latitude=latitude,
    #                                 longitude=longitude)
    #
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserLocationViewSet(viewsets.ModelViewSet):
    queryset = UserLocation.objects.all()
    serializer_class = UserLocationSerializer
    permission_classes = [IsAuthenticated]


from rest_framework.exceptions import APIException


class ServiceUnavailable(APIException):
    status_code = 400
    default_detail = 'Need longitude, latitude, radius in query params'
    default_code = 'longitude_latitude_radius'


class NearestPlacesViewSet(mixins.ListModelMixin,
                           viewsets.GenericViewSet):
    serializer_class = PlaceListSerializer

    def get_queryset(self):
        latitude = self.request.query_params.get('latitude')
        longitude = self.request.query_params.get('longitude')
        radius = float(self.request.query_params.get('radius')) * 1000  # convert to metr

        if not longitude or not latitude or not radius:
            raise ServiceUnavailable()

        pnt = Point(float(longitude), float(latitude), srid=4326)
        return Place.objects.annotate(distance=Distance('location__point', pnt)).filter(distance__lte=radius)


from geopy.geocoders import GeoNames


class GeoPyChooseView(APIView):
    def get(self, request, format=None):
        longitude = request.query_params.get('longitude')
        latitude = request.query_params.get('latitude')
        search = request.query_params.get('search')

        response = []

        if not search:
            return Response(response)
        geo_names = GeoNames(username='travel_attaplace')
        locations = geo_names.geocode(search, exactly_one=False)
        if locations:
            for l in locations:
                response.append(l.raw)
        return Response(response)



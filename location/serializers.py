from django.contrib.gis.geos import Point
from loguru import logger
from rest_framework import serializers
from cities.models import City, District, Country, PostalCode
from rest_framework_gis.serializers import GeometrySerializerMethodField, GeoFeatureModelSerializer

from location.config import geopy_response, place_names, additional_place_names
from location.models import UserLocation, PlaceLocation


class PlaceLocationSerializer(serializers.ModelSerializer):
    # place = serializers.PrimaryKeyRelatedField(required=False, read_only=True)

    class Meta:
        model = PlaceLocation
        fields = '__all__'
        # exclude = ('point',)

    def create(self, validated_data):
        logger.info(validated_data)
        latitude = validated_data.get('latitude')
        longitude = validated_data.get('longitude')
        point = None
        if latitude and longitude:
            point = Point(float(longitude), float(latitude), srid=4326)
        validated_data['point'] = point
        return PlaceLocation.objects.create(**validated_data)


def service_to_location_data(validated_data):
    latitude = validated_data.get('latitude')
    longitude = validated_data.get('longitude')

    response = geopy_response(latitude, longitude)
    logger.warning(response)

    for pn in (place_names + additional_place_names):
        for key in response.keys():
            if pn == key:
                continue
            else:
                validated_data[pn] = None

    for key, value in response.items():
        if key in ('id', 'place_id'):
            continue
        if key == 'ISO3166-2-lvl4':
            validated_data['iso_3166_2_lvl4'] = response[key]
            continue
        if key == 'postcode':
            validated_data['postal_code'] = response[key]
            continue
        if key == 'name':
            logger.info('here')
            validated_data['name'] = response['name']
        if key not in (place_names + additional_place_names):
            continue
        validated_data[key] = value

    point = None
    if latitude and longitude:
        point = Point(float(longitude), float(latitude), srid=4326)
    validated_data['point'] = point

    return validated_data


class UserLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLocation
        fields = '__all__'
        # exclude = ('point',)

    def create(self, validated_data):
        validated_data = service_to_location_data(validated_data)
        return UserLocation.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        if instance.latitude != validated_data['latitude'] or instance.longitude != validated_data['longitude']:
            validated_data = service_to_location_data(validated_data)

        return super(UserLocationSerializer, self).update(instance, validated_data)


class LocationSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    country_name = serializers.CharField()
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()
    # location = GeometrySerializerMethodField()


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class PostalCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostalCode
        fields = '__all__'

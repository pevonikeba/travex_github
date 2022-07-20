from django.contrib.gis.geos import Point
from loguru import logger
from rest_framework import serializers
from cities.models import City, District, Country, PostalCode
from rest_framework_gis.serializers import GeometrySerializerMethodField, GeoFeatureModelSerializer

from location.models import UserLocation, PlaceLocation


class PlaceLocationSerializer(serializers.ModelSerializer):
    place = serializers.PrimaryKeyRelatedField(required=False, read_only=True)

    class Meta:
        model = PlaceLocation
        fields = '__all__'
        # exclude = ('point',)

    def create(self, validated_data):
        latitude = validated_data.get('latitude')
        longitude = validated_data.get('longitude')
        point = None
        if latitude and longitude:
            point = Point(float(longitude), float(latitude), srid=4326)
        validated_data['point'] = point
        return PlaceLocation.objects.create(**validated_data)


class UserLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLocation
        fields = '__all__'
        # exclude = ('point',)

    def create(self, validated_data):
        latitude = validated_data.get('latitude')
        longitude = validated_data.get('longitude')
        point = None
        if latitude and longitude:
            point = Point(float(longitude), float(latitude), srid=4326)
        validated_data['point'] = point
        return UserLocation.objects.create(**validated_data)


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

from rest_framework import serializers
from cities.models import City, District, Country, PostalCode
from rest_framework_gis.serializers import GeometrySerializerMethodField


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

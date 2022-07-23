from loguru import logger
from rest_framework import serializers

from location.models import PlaceLocation
from location.serializers import PlaceLocationSerializer
from place.models import Place, CustomUser
from place.serializers.config import location_model_fields


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'image', )


class PlaceCreateSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    writer_user = CustomUserSerializer(default=serializers.CurrentUserDefault())
    location = PlaceLocationSerializer()

    class Meta:
        model = Place
        fields = ('id', 'writer_user', 'location',) + location_model_fields
        depth = 1

    def create(self, validated_data):
        location_data = validated_data.pop('location', None)
        place = Place.objects.create(**validated_data)
        logger.info(place)
        logger.warning(validated_data)
        if location_data:
            PlaceLocation.objects.create(place=place, **location_data)
        return place

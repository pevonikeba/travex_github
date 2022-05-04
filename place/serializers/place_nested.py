from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers
from place.models import Transport, PlaceImage


class TransportSerializer(serializers.ModelSerializer):
    image = Base64ImageField(required=False)

    class Meta:
        model = Transport
        fields = [field.name for field in model._meta.fields]
        fields.append('image')


class PlaceImageSerializer(serializers.ModelSerializer):
    image = Base64ImageField()  # From DRF Extra Fields

    class Meta:
        model = PlaceImage
        fields = [field.name for field in model._meta.fields]
        fields.append('image')

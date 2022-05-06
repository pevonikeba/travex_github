from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from place.models import Transport, PlaceImage, MustSee, AccommodationOption, Category, FloraFauna


class TransportSerializer(serializers.ModelSerializer):
    # image = Base64ImageField(required=False)

    class Meta:
        model = Transport
        fields = [field.name for field in model._meta.fields]
        # fields.append('image')


class PlaceImageSerializer(serializers.ModelSerializer):
    # image = Base64ImageField(required=False)  # From DRF Extra Fields

    class Meta:
        model = PlaceImage
        fields = [field.name for field in model._meta.fields]
        # fields.append('image')


class MustSeeSerializer(ModelSerializer):
    image = Base64ImageField(required=False)  # From DRF Extra Fields

    class Meta:
        model = MustSee
        fields = [field.name for field in model._meta.fields]
        fields.append('image')


class AccommodationOptionSerializer(ModelSerializer):
    class Meta:
        model = AccommodationOption
        fields = [field.name for field in model._meta.fields]


class CategorySerializer(ModelSerializer):
    # image = Base64ImageField(required=False)  # From DRF Extra Fields

    class Meta:
        model = Category
        fields = [field.name for field in model._meta.fields]
        # fields.append('image')
        fields.append('places')


class FloraFaunaSerializer(ModelSerializer):
    image = Base64ImageField(required=False)  # From DRF Extra Fields

    class Meta:
        model = FloraFauna
        fields = [field.name for field in model._meta.fields]
        fields.append('image')


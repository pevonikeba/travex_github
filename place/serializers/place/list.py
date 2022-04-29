from rest_framework import serializers
from place.models import Place, CustomUser, PlaceImage


class PlaceImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceImage
        fields = ('id', 'image',)


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'image',)


class PlaceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ('id', 'name', 'description', 'place_images', 'rating', 'locations', 'writer_user',)
        depth = 1

    writer_user = CustomUserSerializer()
    place_images = PlaceImageSerializer(many=True)

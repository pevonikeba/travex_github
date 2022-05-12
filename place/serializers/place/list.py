from rest_framework import serializers
from place.models import Place, CustomUser, PlaceImage
from place.serializers.place_nested import PlaceImageSerializer


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'image',)


class PlaceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ('id', 'name', 'is_bookmarked', 'description', 'place_images', 'rating', 'locations', 'writer_user', 'home_page',)
        depth = 1

    writer_user = CustomUserSerializer()
    place_images = PlaceImageSerializer(many=True)

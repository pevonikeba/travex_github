from rest_framework import serializers
from place.models import Place, CustomUser, Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'path',)


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'image',)


class PlaceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ('id', 'name', 'description', 'images', 'rating', 'locations', 'writer_user',)
        depth = 1

    writer_user = CustomUserSerializer()
    images = ImageSerializer(many=True)

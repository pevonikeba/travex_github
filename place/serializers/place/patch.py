from rest_framework import serializers
from place.models import Place, CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'image',)


class PlaceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ('id', 'writer_user',)
        depth = 1

    writer_user = CustomUserSerializer(default=serializers.CurrentUserDefault())


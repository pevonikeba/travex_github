from rest_framework import serializers
from place.models import Place, CustomUser
from place.serializers.config import location_model_fields


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'image', )


class PlaceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ('id', 'writer_user', ) + location_model_fields
        depth = 1
    id = serializers.ReadOnlyField()
    writer_user = CustomUserSerializer(default=serializers.CurrentUserDefault())

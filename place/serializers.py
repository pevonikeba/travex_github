from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from place.models import Place, Group, Image


class PlaceSerializer(ModelSerializer):

    images = serializers.StringRelatedField(many=True)

    class Meta:
        model = Place
        fields = '__all__'

class GroupSerializer(ModelSerializer):

    places = PlaceSerializer(many=True, read_only=True)

    class Meta:
        model = Group
        fields = '__all__'



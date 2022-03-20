from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from place.models import Place, Group, Image, ClimaticConditions, TypeOfTerrain


class PlaceSerializer(ModelSerializer):
    locations = serializers.StringRelatedField(many=True)
    images = serializers.StringRelatedField(many=True)
    transports = serializers.StringRelatedField(many=True)
    accommodationOptions = serializers.StringRelatedField(many=True)
    uniqueness_place = serializers.StringRelatedField(many=True)
    must_see = serializers.StringRelatedField(many=True)
    where_to_take_a_picture = serializers.StringRelatedField(many=True)
    cuisines = serializers.StringRelatedField(many=True)
    turists = serializers.StringRelatedField(many=True)
    civilizations = serializers.StringRelatedField(many=True)
    safes = serializers.StringRelatedField(many=True)
    entertainments = serializers.StringRelatedField(many=True)
    natural_phenomena = serializers.StringRelatedField(many=True)
    socializations = serializers.StringRelatedField(many=True)
    vibes = serializers.StringRelatedField(many=True)
    flora_fauna = serializers.StringRelatedField(many=True)

    class Meta:
        model = Place
        fields = '__all__'

class GroupSerializer(ModelSerializer):

    places = PlaceSerializer(many=True, read_only=True)

    class Meta:
        model = Group
        fields = '__all__'

class ClimateSerializer(ModelSerializer):

    class Meta:
        model = ClimaticConditions
        fields = '__all__'

class TypeOfTerrainSerializer(ModelSerializer):

    class Meta:
        model = TypeOfTerrain
        fields = '__all__'


from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from place.models import Place, Group, Image


class PlaceSerializer(ModelSerializer):
    locations = serializers.StringRelatedField(many=True)
    images = serializers.StringRelatedField(many=True)
    transports = serializers.StringRelatedField(many=True)
    accommodationOptions = serializers.StringRelatedField(many=True)
    uniqueness_place = serializers.StringRelatedField(many=True)
    must_see = serializers.StringRelatedField(many=True)
    where_to_take_a_picture = serializers.StringRelatedField(many=True)

    class Meta:
        model = Place
        fields = '__all__'

class GroupSerializer(ModelSerializer):

    places = PlaceSerializer(many=True, read_only=True)

    class Meta:
        model = Group
        fields = '__all__'


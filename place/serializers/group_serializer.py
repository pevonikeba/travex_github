from rest_framework.serializers import ModelSerializer

from place.models import Group
from place.serializers.place.list import PlaceListSerializer


class GroupSerializer(ModelSerializer):
    places = PlaceListSerializer(many=True, read_only=True)

    class Meta:
        model = Group
        fields = '__all__'

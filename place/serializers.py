from rest_framework.serializers import ModelSerializer

from place.models import Place, Groups


class PlaceSerializer(ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'

class GroupSerializer(ModelSerializer):
    class Meta:
        model = Groups
        fields = '__all__'



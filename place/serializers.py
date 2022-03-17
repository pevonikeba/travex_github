from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from place.models import Place, Group, Transport, AccommodationOptions, UniquenessPlace, MustSee, WhereToTakeAPicture


class TransportSerializer(ModelSerializer):

    class Meta:
        model = Transport
        fields = '__all__'

class AccommodationOptionsSerializer(ModelSerializer):

    class Meta:
        model = AccommodationOptions
        fields = '__all__'

class UniquenessPlaceSerializer(ModelSerializer):

    class Meta:
        model = UniquenessPlace
        fields = '__all__'

class MustSeeSerializer(ModelSerializer):

    class Meta:
        model = MustSee
        fields = '__all__'

class WhereToTakeAPictureSerializer(ModelSerializer):

    class Meta:
        model = WhereToTakeAPicture
        fields = '__all__'



class PlaceSerializer(ModelSerializer):

    images = serializers.StringRelatedField(many=True)
    transports = TransportSerializer(many=True, read_only=True)
    accommodationOptions = AccommodationOptionsSerializer(many=True, read_only=True)
    uniqueness_place = UniquenessPlaceSerializer(many=True, read_only=True)
    must_see = MustSeeSerializer(many=True, read_only=True)
    where_to_take_a_picture = WhereToTakeAPictureSerializer(many=True, read_only=True)

    class Meta:
        model = Place
        fields = '__all__'

class GroupSerializer(ModelSerializer):

    places = PlaceSerializer(many=True, read_only=True)

    class Meta:
        model = Group
        fields = '__all__'


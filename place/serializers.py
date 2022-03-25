from django_countries.serializers import CountryFieldMixin
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from place.models import Place, Group, Image, ClimaticConditions, TypeOfTerrain, TypeOfPeople, Location, \
    FloraAndFauna, WhereToTakeAPicture, Vibe, MustSee, UniquenessPlace, AccommodationOptions, \
    NaturalPhenomena, Entertainment, Cuisine, Safe, Transport, Category, UserPlaceRelation, InterestingFacts


class LocationSerializer(CountryFieldMixin, ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class TransportSerializer(ModelSerializer):
    class Meta:
        model = Transport
        fields = '__all__'


class SafeSerializer(ModelSerializer):
    class Meta:
        model = Safe
        fields = '__all__'



class CuisineSerializer(ModelSerializer):
    class Meta:
        model = Cuisine
        fields = '__all__'


class EntertainmentSerializer(ModelSerializer):
    class Meta:
        model = Entertainment
        fields = '__all__'


class NaturalPhenomenaSerializer(ModelSerializer):
    class Meta:
        model = NaturalPhenomena
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


class VibeSerializer(ModelSerializer):
    class Meta:
        model = Vibe
        fields = '__all__'


class WhereToTakeAPictureSerializer(ModelSerializer):
    class Meta:
        model = WhereToTakeAPicture
        fields = '__all__'


class FloraAndFaunaSerializer(ModelSerializer):
    class Meta:
        model = FloraAndFauna
        fields = '__all__'

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class InterestingFactsSerializer(ModelSerializer):
    class Meta:
        model = InterestingFacts
        fields = '__all__'


class PlaceSerializer(ModelSerializer):

    writer_user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    categories = CategorySerializer(many=True, read_only=True)

    images = serializers.StringRelatedField(many=True)

    locations = LocationSerializer(many=True, read_only=True)
    transports = TransportSerializer(many=True)
    accommodationOptions = AccommodationOptionsSerializer(many=True)
    uniqueness_place = UniquenessPlaceSerializer(many=True)
    must_see = MustSeeSerializer(many=True)
    where_to_take_a_picture = WhereToTakeAPictureSerializer(many=True)
    cuisines = CuisineSerializer(many=True)
    safes = SafeSerializer(many=True)
    entertainments = EntertainmentSerializer(many=True)
    natural_phenomena = NaturalPhenomenaSerializer(many=True)
    vibes = VibeSerializer(many=True)
    interesting_facts = InterestingFactsSerializer(many=True)
    flora_fauna = FloraAndFaunaSerializer(many=True)

    class Meta:
        model = Place
        fields = '__all__'

class UserPlaceRelationSerializer(ModelSerializer):
    class Meta:
        model = UserPlaceRelation
        fields = ('place', 'in_bookmarks', 'rating', 'description_rating')


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

class TypeOfPeopleSerializer(ModelSerializer):

    civilizations = serializers.StringRelatedField(many=True)

    class Meta:
        model = TypeOfPeople
        fields = '__all__'


from django_countries.serializers import CountryFieldMixin
from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from place.models import Place, Group, Image, ClimaticConditions, TypeOfTerrain, TypeOfPeople, Location, \
    FloraAndFauna, WhereToTakeAPicture, Vibe, MustSee, UniquenessPlace, AccommodationOptions, \
    NaturalPhenomena, Entertainment, Cuisine, Safe, Transport, Category, UserPlaceRelation, InterestingFacts



class LocationSerializer(CountryFieldMixin, ModelSerializer):
    class Meta:
        model = Location
        fields = ('continent', 'country', 'region', 'city', 'latitude', 'longitude', 'nearest_place',)


class TransportSerializer(ModelSerializer):
    image = Base64ImageField()  # From DRF Extra Fields

    class Meta:
        model = Transport
        fields = ('name', 'price', 'description', 'comfortable', 'image',)

    def create(self, validated_data):

        image = validated_data.pop('image')
        data = validated_data.pop('data')

        return Transport.objects.create(data=data, image=image)


class SafeSerializer(ModelSerializer):
    class Meta:
        model = Safe
        fields = ('name', 'how_dangerous', 'rating_danger', 'description',)


class CuisineSerializer(ModelSerializer):
    image = Base64ImageField()  # From DRF Extra Fields

    class Meta:
        model = Cuisine
        fields = ('name', 'type_cuisine', 'description', 'image', 'price',)

    def create(self, validated_data):
        image = validated_data.pop('image')
        data = validated_data.pop('data')

        return Cuisine.objects.create(data=data, image=image)


class EntertainmentSerializer(ModelSerializer):
    image = Base64ImageField()  # From DRF Extra Fields

    class Meta:
        model = Entertainment
        fields = ('name', 'description', 'image',)

    def create(self, validated_data):
        image = validated_data.pop('image')
        data = validated_data.pop('data')

        return Entertainment.objects.create(data=data, image=image)


class NaturalPhenomenaSerializer(ModelSerializer):
    image = Base64ImageField()  # From DRF Extra Fields

    class Meta:
        model = NaturalPhenomena
        fields = ('name', 'description', 'image',)

    def create(self, validated_data):
        image = validated_data.pop('image')
        data = validated_data.pop('data')

        return NaturalPhenomena.objects.create(data=data, image=image)


class AccommodationOptionsSerializer(ModelSerializer):
    class Meta:
        model = AccommodationOptions
        fields = ('name', 'price', 'description',)


class UniquenessPlaceSerializer(ModelSerializer):
    image = Base64ImageField()  # From DRF Extra Fields

    class Meta:
        model = UniquenessPlace
        fields = ('name', 'description', 'image',)

    def create(self, validated_data):
        image = validated_data.pop('image')
        data = validated_data.pop('data')

        return UniquenessPlace.objects.create(data=data, image=image)


class MustSeeSerializer(ModelSerializer):
    image = Base64ImageField()  # From DRF Extra Fields

    class Meta:
        model = MustSee
        fields = ('name', 'description', 'image',)

    def create(self, validated_data):
        image = validated_data.pop('image')
        data = validated_data.pop('data')

        return MustSee.objects.create(data=data, image=image)


class VibeSerializer(ModelSerializer):
    image = Base64ImageField()  # From DRF Extra Fields

    class Meta:
        model = Vibe
        fields = ('vibe', 'image',)

    def create(self, validated_data):
        image = validated_data.pop('image')
        data = validated_data.pop('data')

        return Vibe.objects.create(data=data, image=image)


class WhereToTakeAPictureSerializer(ModelSerializer):
    image = Base64ImageField()  # From DRF Extra Fields

    class Meta:
        model = WhereToTakeAPicture
        fields = ('name', 'description', 'image',)

    def create(self, validated_data):
        image = validated_data.pop('image')
        data = validated_data.pop('data')

        return WhereToTakeAPicture.objects.create(data=data, image=image)


class FloraAndFaunaSerializer(ModelSerializer):
    image = Base64ImageField()  # From DRF Extra Fields

    class Meta:
        model = FloraAndFauna
        fields = ('name', 'description', 'image',)

    def create(self, validated_data):
        image = validated_data.pop('image')
        data = validated_data.pop('data')

        return FloraAndFauna.objects.create(data=data, image=image)



class InterestingFactsSerializer(ModelSerializer):
    image = Base64ImageField()  # From DRF Extra Fields

    class Meta:
        model = InterestingFacts
        fields = ('description', 'image',)

    def create(self, validated_data):
        image = validated_data.pop('image')
        data = validated_data.pop('data')

        return InterestingFacts.objects.create(data=data, image=image)

class ImageSerializer(ModelSerializer):
    path = Base64ImageField()  # From DRF Extra Fields
    class Meta:
        model = Image
        fields = ('path',)

    def create(self, validated_data):
        image = validated_data.pop('path')
        return Image.objects.create(image=image)



class CategorySerializer(ModelSerializer):
    image = Base64ImageField()  # From DRF Extra Fields


    class Meta:
        model = Category
        fields = '__all__'

    def create(self, validated_data):
        image = validated_data.pop('image')
        data = validated_data.pop('data')

        return Category.objects.create(data=data, image=image)


class PlaceSerializer(ModelSerializer):
    id = serializers.ReadOnlyField()
    writer_user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    category = CategorySerializer(many=True, required=False)

    # images = serializers.StringRelatedField(many=True, required=False)

    images = ImageSerializer(many=True, required=False)

    locations = LocationSerializer(many=True, required=False)
    transports = TransportSerializer(many=True, required=False)
    accommodationOptions = AccommodationOptionsSerializer(many=True, required=False)
    uniqueness_place = UniquenessPlaceSerializer(many=True, required=False)
    must_see = MustSeeSerializer(many=True, required=False)
    where_to_take_a_picture = WhereToTakeAPictureSerializer(many=True, required=False)
    cuisines = CuisineSerializer(many=True, required=False)
    safes = SafeSerializer(many=True, required=False)
    entertainments = EntertainmentSerializer(many=True, required=False)
    natural_phenomena = NaturalPhenomenaSerializer(many=True, required=False)
    vibes = VibeSerializer(many=True, required=False)
    interesting_facts = InterestingFactsSerializer(many=True, required=False)
    flora_fauna = FloraAndFaunaSerializer(many=True, required=False)

    class Meta:
        model = Place
        fields = '__all__'

    def create(self, validated_data):
        category_data = validated_data.pop('category')
        images_data = validated_data.pop('images')
        locations_data = validated_data.pop('locations')
        transports_data = validated_data.pop('transports')
        accommodationOptions_data = validated_data.pop('accommodationOptions')
        uniqueness_place_data = validated_data.pop('uniqueness_place')
        must_see_data = validated_data.pop('must_see')
        where_to_take_a_picture_data = validated_data.pop('where_to_take_a_picture')
        cuisines_data = validated_data.pop('cuisines')
        safes_data = validated_data.pop('safes')
        entertainments_data = validated_data.pop('entertainments')
        natural_phenomena_data = validated_data.pop('natural_phenomena')
        vibes_data = validated_data.pop('vibes')
        interesting_facts_data = validated_data.pop('interesting_facts')
        flora_fauna_data = validated_data.pop('flora_fauna')

        place = Place.objects.create(**validated_data)

        for image_data in images_data:
            Image.objects.create(place=place, **image_data)
        for categor_data in category_data:
            Category.objects.get_or_create(place=place, **categor_data)
        for item in locations_data:
            Location.objects.create(place=place, **item)
        for transport_data in transports_data:
            Transport.objects.create(place=place, **transport_data)
        for accommodationOption_data in accommodationOptions_data:
            AccommodationOptions.objects.create(place=place, **accommodationOption_data)
        for uniquenes_place_data in uniqueness_place_data:
            UniquenessPlace.objects.create(place=place, **uniquenes_place_data)
        for must_se_data in must_see_data:
            MustSee.objects.create(place=place, **must_se_data)
        for where_to_take_a_pictur_data in where_to_take_a_picture_data:
            WhereToTakeAPicture.objects.create(place=place, **where_to_take_a_pictur_data)
        for cuisine_data in cuisines_data:
            Cuisine.objects.create(place=place, **cuisine_data)
        for safe_data in safes_data:
            Safe.objects.create(place=place, **safe_data)
        for entertainment_data in entertainments_data:
            Entertainment.objects.create(place=place, **entertainment_data)
        for natural_phenomen_data in natural_phenomena_data:
            NaturalPhenomena.objects.create(place=place, **natural_phenomen_data)
        for vibe_data in vibes_data:
            Vibe.objects.create(place=place, **vibe_data)
        for interesting_fact_data in interesting_facts_data:
            InterestingFacts.objects.create(place=place, **interesting_fact_data)
        for flora_faun_data in flora_fauna_data:
            FloraAndFauna.objects.create(place=place, **flora_faun_data)
        return place







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


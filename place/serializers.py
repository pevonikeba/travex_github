from dj_rest_auth.registration.serializers import SocialLoginSerializer
from django.contrib.auth.hashers import make_password
from django_countries.serializers import CountryFieldMixin
from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from place.models import Place, Group, Image, ClimaticConditions, \
    FloraAndFauna, WhereToTakeAPicture, Vibe, MustSee, UniquenessPlace, AccommodationOptions, \
    NaturalPhenomena, Entertainment, Cuisine, Safe, Transport, Category, UserPlaceRelation, InterestingFacts, \
    GeographicalFeature, PracticalInformation, TypeTransport, TypeCuisine, CustomUser, Bookmark, Location



class CustomUserSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    password = serializers.CharField(max_length=255, write_only=True)
    # is_active = serializers.BooleanField()

    class Meta:
        model = CustomUser

        fields = ('id', 'email', 'username', 'image', 'is_active', 'password', 'user')

    # def validate_password(self, value: str) -> str:
    #     """
    #     Hash value passed by user.
    #
    #     :param value: password of a user
    #     :return: a hashed version of the password
    #     """
    #     return make_password(value)

    def create(self, validated_data):
        validated_data['is_active'] = False
        user = super().create(validated_data)

        user.set_password(validated_data['password'])
        user.save()
        return user

class BookmarkSerializer(ModelSerializer):
    class Meta:
        model = Bookmark
        fields = ('id', 'user', 'place')

class BookmarkPlaceSerializer(ModelSerializer):
    class Meta:
        model = Bookmark
        fields = ('id', "user",)

class BookmarkUserSerializer(ModelSerializer):
    place = serializers.SerializerMethodField()
    class Meta:
        model = Bookmark
        fields = ('id', "place",)

    def create(self, request):
        serializer = BookmarkUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()



class CustomSocialLoginSerializer(SocialLoginSerializer):
    access = serializers.CharField(source='access_token')

    class Meta:
        fields = ('__all__', 'access')


class LocationSerializer(CountryFieldMixin, ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'continent', 'country', 'state', 'city', 'latitude', 'longitude', 'nearest_place',)

class TypeTransportSerializer(ModelSerializer):
    class Meta:
        model = TypeTransport
        fields = ('id', 'name',)


class TransportSerializer(ModelSerializer):
    image = Base64ImageField()  # From DRF Extra Fields
    # name = TypeTransportSerializer(many=True, read_only=True)
    name = serializers.CharField(source='name.name')
    class Meta:
        model = Transport
        fields = ('id', 'name', 'price', 'description', 'comfortable', 'image',)

    def create(self, validated_data):

        image = validated_data.pop('image')
        data = validated_data.pop('data')

        return Transport.objects.create(data=data, image=image)


class SafeSerializer(ModelSerializer):
    class Meta:
        model = Safe
        fields = ('id', 'name', 'how_dangerous', 'rating_danger', 'description',)

class TypeCuisineSerializer(ModelSerializer):
    class Meta:
        model = TypeCuisine
        fields = ('id', 'type',)

class CuisineSerializer(ModelSerializer):
    image = Base64ImageField()  # From DRF Extra Fields
    # name = TypeCuisineSerializer(many=True, required=False, read_only=True)
    name = serializers.CharField(source='name.type')


    class Meta:
        model = Cuisine
        fields = ('id', 'name', 'description', 'image', 'price',)

    def create(self, validated_data):
        # name_data = validated_data.pop('name')
        image = validated_data.pop('image')
        data = validated_data.pop('data')

        cuisine = Cuisine.objects.create(data=data, image=image)

        # cuisine.name.set(name_data)

        return cuisine



class EntertainmentSerializer(ModelSerializer):
    image = Base64ImageField()  # From DRF Extra Fields

    class Meta:
        model = Entertainment
        fields = ('id', 'name', 'description', 'image',)

    def create(self, validated_data):
        image = validated_data.pop('image')
        data = validated_data.pop('data')

        return Entertainment.objects.create(data=data, image=image)


class NaturalPhenomenaSerializer(ModelSerializer):
    image = Base64ImageField()  # From DRF Extra Fields

    class Meta:
        model = NaturalPhenomena
        fields = ('id', 'name', 'description', 'image',)

    def create(self, validated_data):
        image = validated_data.pop('image')
        data = validated_data.pop('data')

        return NaturalPhenomena.objects.create(data=data, image=image)


class AccommodationOptionsSerializer(ModelSerializer):
    class Meta:
        model = AccommodationOptions
        fields = ('id', 'name', 'price', 'description',)


class UniquenessPlaceSerializer(ModelSerializer):
    image = Base64ImageField()  # From DRF Extra Fields

    class Meta:
        model = UniquenessPlace
        fields = ('id', 'name', 'description', 'image',)

    def create(self, validated_data):
        image = validated_data.pop('image')
        data = validated_data.pop('data')

        return UniquenessPlace.objects.create(data=data, image=image)


class MustSeeSerializer(ModelSerializer):
    image = Base64ImageField()  # From DRF Extra Fields

    class Meta:
        model = MustSee
        fields = ('id', 'name', 'description', 'image',)

    def create(self, validated_data):
        image = validated_data.pop('image')
        data = validated_data.pop('data')

        return MustSee.objects.create(data=data, image=image)


class VibeSerializer(ModelSerializer):
    image = Base64ImageField()  # From DRF Extra Fields

    class Meta:
        model = Vibe
        fields = ('id', 'name', 'image',)

    def create(self, validated_data):
        image = validated_data.pop('image')
        data = validated_data.pop('data')

        return Vibe.objects.create(data=data, image=image)


class WhereToTakeAPictureSerializer(ModelSerializer):
    image = Base64ImageField()  # From DRF Extra Fields

    class Meta:
        model = WhereToTakeAPicture
        fields = ('id', 'name', 'description', 'image',)

    def create(self, validated_data):
        image = validated_data.pop('image')
        data = validated_data.pop('data')

        return WhereToTakeAPicture.objects.create(data=data, image=image)


class FloraAndFaunaSerializer(ModelSerializer):
    image = Base64ImageField()  # From DRF Extra Fields

    class Meta:
        model = FloraAndFauna
        fields = ('id', 'name', 'description', 'image',)

    def create(self, validated_data):
        image = validated_data.pop('image')
        data = validated_data.pop('data')

        return FloraAndFauna.objects.create(data=data, image=image)



class InterestingFactsSerializer(ModelSerializer):
    image = Base64ImageField()  # From DRF Extra Fields

    class Meta:
        model = InterestingFacts
        fields = ('id', 'description', 'image',)

    def create(self, validated_data):
        image = validated_data.pop('image')
        data = validated_data.pop('data')

        return InterestingFacts.objects.create(data=data, image=image)

class PracticalInformationSerializer(ModelSerializer):
    class Meta:
        model = PracticalInformation
        fields = ('id', 'description',)


class ImageSerializer(ModelSerializer):
    path = Base64ImageField()  # From DRF Extra Fields
    class Meta:
        model = Image
        fields = ('id', 'path',)

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

    class Meta:
        model = Place
        fields = '__all__'


    id = serializers.ReadOnlyField()
    writer_user = CustomUserSerializer(default=serializers.CurrentUserDefault())
    # print('writer_user: ', writer_user)
    # writer_user = CustomUserSerializer(many=True, read_only=True)

    bookmark = BookmarkPlaceSerializer(many=True, read_only=True)

    # category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), many=True)
    category = CategorySerializer(many=True, required=False)

    # images = serializers.StringRelatedField(many=True, required=False)
    images = ImageSerializer(many=True, required=False)

    location = LocationSerializer(many=True, required=False)
    transport = TransportSerializer(many=True, required=False)
    accommodation_Option = AccommodationOptionsSerializer(many=True, required=False)
    uniqueness_place = UniquenessPlaceSerializer(many=True, required=False)
    must_see = MustSeeSerializer(many=True, required=False)
    where_to_take_a_picture = WhereToTakeAPictureSerializer(many=True, required=False)
    cuisine = CuisineSerializer(many=True, required=False)
    safes = SafeSerializer(many=True, required=False)
    entertainment = EntertainmentSerializer(many=True, required=False)
    natural_phenomena = NaturalPhenomenaSerializer(many=True, required=False)
    vibe = VibeSerializer(many=True, required=False)
    interesting_fact = InterestingFactsSerializer(many=True, required=False)
    practical_information = PracticalInformationSerializer(many=True, required=False)
    flora_fauna = FloraAndFaunaSerializer(many=True, required=False)


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
        practical_information_data = validated_data.pop('practical_informations')
        flora_fauna_data = validated_data.pop('flora_fauna')

        place = Place.objects.create(**validated_data)
        place.category.set(category_data)

        for image_data in images_data:
            Image.objects.create(place=place, **image_data)
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
        for item in practical_information_data:
            PracticalInformation.objects.create(place=place, **item)
        for flora_faun_data in flora_fauna_data:
            FloraAndFauna.objects.create(place=place, **flora_faun_data)
        return place




class ClimateSerializer(ModelSerializer):

    class Meta:
        model = ClimaticConditions
        fields = '__all__'

class GeographicalFeatureSerializer(ModelSerializer):

    class Meta:
        model = GeographicalFeature
        fields = '__all__'


class UserPlaceRelationSerializer(ModelSerializer):
    class Meta:
        model = UserPlaceRelation
        fields = ('id', 'place', 'in_bookmarks', 'rating', 'description_rating')



class GroupSerializer(ModelSerializer):

    place = PlaceSerializer(many=True, read_only=True)

    class Meta:
        model = Group
        fields = '__all__'




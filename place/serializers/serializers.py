from loguru import logger

from django_countries.serializers import CountryFieldMixin
from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from rest_framework_simplejwt.tokens import RefreshToken

from place.models import Place, Group, PlaceImage, ClimaticCondition, \
    FloraFauna, WhereToTakeAPicture, Vibe, MustSee, UniquenessPlace, AccommodationOption, \
    NaturalPhenomena, Entertainment, Cuisine, Safe, Transport, Category, UserPlaceRelation, InterestingFacts, \
    GeographicalFeature, PracticalInformation, TypeTransport, TypeCuisine, CustomUser, Location, Bookmark, \
    ClimaticConditiomm
from place.serializers.place.list import PlaceListSerializer
from place.serializers.place_nested import PlaceImageSerializer, TransportSerializer, MustSeeSerializer, \
    AccommodationOptionSerializer, FloraFaunaSerializer


class CustomUserImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('image',)


class CustomUserPatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('name', 'last_name', 'age', 'gender', 'language', 'image', 'image_social', )


class CustomUserSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    password = serializers.CharField(max_length=255, write_only=True)
    # is_active = serializers.BooleanField()

    class Meta:
        model = CustomUser

        fields = ('id', 'email', 'username', 'image', 'is_active', 'password', 'user', 'image_social',)

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
    place = PlaceListSerializer()
    writer_user = CustomUserSerializer(default=serializers.CurrentUserDefault())

    class Meta:
        model = Bookmark
        fields = ('id', 'writer_user', 'place')

    # def create(self, validated_data):
    #     user_data = validated_data.pop('user')
    #     place_data = validated_data.pop('place')
    #     if Bookmark.objects.filter(user=user_data, place=place_data).exists():
    #         bookmark = Bookmark.objects.get(user=user_data, place=place_data)
    #         bookmark.delete()
    #         bookmark.save()
    #         return bookmark

        # user = User.objects.create(**validated_data)
        # Profile.objects.create(user=user, **profile_data)
        # return user

# class BookmarkPlaceSerializer(ModelSerializer):
#     class Meta:
#         model = Bookmark
#         fields = ('id', "user",)
#
#
# class BookmarkUserSerializer(ModelSerializer):
#     place = serializers.SerializerMethodField()
#
#     class Meta:
#         model = Bookmark
#         fields = ('id', "place",)
#
#     def create(self, request):
#         serializer = BookmarkUserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()


# class TokenObtainLifetimeSerializer(TokenObtainPairSerializer):
#     def validate(self, attrs):
#         data = super().validate(attrs)
#         refresh = self.get_token(self.user)
#         data['lifetime'] = int(refresh.access_token.lifetime.total_seconds())
#         return data
#
#
# class TokenRefreshLifetimeSerializer(TokenRefreshSerializer):
#     def validate(self, attrs):
#         data = super().validate(attrs)
#         refresh = RefreshToken(attrs['refresh'])
#         data['lifetime'] = int(refresh.access_token.lifetime.total_seconds())
#         return data

class LocationSerializer(CountryFieldMixin, ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"


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


class UniquenessPlaceSerializer(ModelSerializer):
    image = Base64ImageField()  # From DRF Extra Fields

    class Meta:
        model = UniquenessPlace
        fields = ('id', 'name', 'description', 'image',)

    def create(self, validated_data):
        image = validated_data.pop('image')
        data = validated_data.pop('data')

        return UniquenessPlace.objects.create(data=data, image=image)


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


class TypeTransportSerializer(ModelSerializer):
    class Meta:
        model = TypeTransport
        fields = ('id', 'name',)


# class TransportSerializer(ModelSerializer):
#     image = Base64ImageField(required=False)  # From DRF Extra Fields
#     # name = TypeTransportSerializer(many=True, read_only=True)
#     # name = serializers.CharField(source='name.name')
#
#     class Meta:
#         model = Transport
#         fields = ('id', 'type_transport', 'price', 'description', 'comfortable', 'image', 'place',)
#
#     def create(self, validated_data):
#         image = validated_data.pop('image')
#         data = validated_data.pop('data')
#
#         return Transport.objects.create(data=data, image=image)

# class PlaceImageSerializer(ModelSerializer):
#     image = Base64ImageField()  # From DRF Extra Fields
#
#     class Meta:
#         model = PlaceImage
#         fields = ('id', 'image', 'place',)
#
#
class PlaceSerializer(ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'

    id = serializers.ReadOnlyField()
    writer_user = CustomUserSerializer(default=serializers.CurrentUserDefault())
    # bookmarks = BookmarkPlaceSerializer(many=True, read_only=True)
    categories = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), many=True, required=False)
    # images = serializers.StringRelatedField(many=True, required=False)
    place_images = PlaceImageSerializer(many=True, required=False)
    locations = LocationSerializer()
    transports = TransportSerializer(many=True, required=False)
    accommodation_options = AccommodationOptionSerializer(many=True, required=False)
    uniqueness_places = UniquenessPlaceSerializer(many=True, required=False)
    must_sees = MustSeeSerializer(many=True, required=False)
    where_to_take_a_pictures = WhereToTakeAPictureSerializer(many=True, required=False)
    cuisines = CuisineSerializer(many=True, required=False)
    safes = SafeSerializer(many=True, required=False)
    entertainments = EntertainmentSerializer(many=True, required=False)
    natural_phenomenas = NaturalPhenomenaSerializer(many=True, required=False)
    vibes = VibeSerializer(many=True, required=False)
    interesting_facts = InterestingFactsSerializer(many=True, required=False)
    practical_informations = PracticalInformationSerializer(many=True, required=False)
    flora_faunas = FloraFaunaSerializer(many=True, required=False)

    def create(self, validated_data):
        logger.info("create")
        transports_data = None
        category_data = validated_data.get('category')
        place_images_data = validated_data.get('place_images')
        locations_data = validated_data.get('locations')
        if 'transports' in validated_data:
            transports_data = validated_data.pop('transports')
        accommodationOptions_data = validated_data.get('accommodationOption')
        uniqueness_place_data = validated_data.get('uniqueness_place')
        must_see_data = validated_data.get('must_see')
        where_to_take_a_picture_data = validated_data.get('where_to_take_a_picture')
        cuisines_data = validated_data.get('cuisines')
        safes_data = validated_data.get('safes')
        entertainments_data = validated_data.get('entertainments')
        natural_phenomena_data = validated_data.get('natural_phenomena')
        vibes_data = validated_data.get('vibes')
        interesting_facts_data = validated_data.get('interesting_facts')
        practical_information_data = validated_data.get('practical_informations')
        flora_fauna_data = validated_data.get('flora_fauna')

        #
        place = Place.objects.create(**validated_data)

        if transports_data is not None:
            for item in transports_data:
                Transport.objects.create(place=place, **item)

        if category_data is not None:
            place.category.set(category_data)
        if place_images_data is not None:
            for image_data in place_images_data:
                PlaceImage.objects.create(place=place, **image_data)
        if locations_data is not None:
            for item in locations_data:
                Location.objects.create(place=place, **item)
        # if transports_data is not None:
        #     for transport_data in transports_data:
        #         Transport.objects.create(place=place, **transport_data)
        if accommodationOptions_data is not None:
            for accommodationOption_data in accommodationOptions_data:
                AccommodationOption.objects.create(place=place, **accommodationOption_data)
        if uniqueness_place_data is not None:
            for uniquenes_place_data in uniqueness_place_data:
                UniquenessPlace.objects.create(place=place, **uniquenes_place_data)
        if must_see_data is not None:
            for must_se_data in must_see_data:
                MustSee.objects.create(place=place, **must_se_data)
        if where_to_take_a_picture_data is not None:
            for where_to_take_a_pictur_data in where_to_take_a_picture_data:
                WhereToTakeAPicture.objects.create(place=place, **where_to_take_a_pictur_data)
        if cuisines_data is not None:
            for cuisine_data in cuisines_data:
                Cuisine.objects.create(place=place, **cuisine_data)
        if safes_data is not None:
            for safe_data in safes_data:
                Safe.objects.create(place=place, **safe_data)
        if entertainments_data is not None:
            for entertainment_data in entertainments_data:
                Entertainment.objects.create(place=place, **entertainment_data)
        if natural_phenomena_data is not None:
            for natural_phenomen_data in natural_phenomena_data:
                NaturalPhenomena.objects.create(place=place, **natural_phenomen_data)
        if vibes_data is not None:
            for vibe_data in vibes_data:
                Vibe.objects.create(place=place, **vibe_data)
        if interesting_facts_data is not None:
            for interesting_fact_data in interesting_facts_data:
                InterestingFacts.objects.create(place=place, **interesting_fact_data)
        if practical_information_data is not None:
            for item in practical_information_data:
                PracticalInformation.objects.create(place=place, **item)
        if flora_fauna_data is not None:
            for flora_faun_data in flora_fauna_data:
                FloraFauna.objects.create(place=place, **flora_faun_data)
        return place

# class PlaceSerializer(ModelSerializer):
#
#     class Meta:
#         model = Place
#         fields = '__all__'
#
#
#     id = serializers.ReadOnlyField()
#     writer_user = CustomUserSerializer(default=serializers.CurrentUserDefault())
#     # print('writer_user: ', writer_user)
#     # writer_user = CustomUserSerializer(many=True, read_only=True)
#
#     bookmark = BookmarkPlaceSerializer(many=True, read_only=True)
#
#     # category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), many=True)
#     category = CategorySerializer(many=True, required=False)
#
#     # images = serializers.StringRelatedField(many=True, required=False)
#     images = ImageSerializer(many=True, required=False)
#
#     location = LocationSerializer(many=True, required=False)
#     transport = TransportSerializer(many=True, required=False)
#     accommodation_Option = AccommodationOptionsSerializer(many=True, required=False)
#     uniqueness_place = UniquenessPlaceSerializer(many=True, required=False)
#     must_see = MustSeeSerializer(many=True, required=False)
#     where_to_take_a_picture = WhereToTakeAPictureSerializer(many=True, required=False)
#     cuisine = CuisineSerializer(many=True, required=False)
#     safes = SafeSerializer(many=True, required=False)
#     entertainment = EntertainmentSerializer(many=True, required=False)
#     natural_phenomena = NaturalPhenomenaSerializer(many=True, required=False)
#     vibe = VibeSerializer(many=True, required=False)
#     interesting_fact = InterestingFactsSerializer(many=True, required=False)
#     practical_information = PracticalInformationSerializer(many=True, required=False)
#     flora_fauna = FloraFaunaSerializer(many=True, required=False)
#
#     # TODO: not working
#     def create(self, validated_data):
#         print('create aaaa: ')
#         category_data = validated_data.pop('category')
#         images_data = validated_data.pop('images')
#         locations_data = validated_data.pop('locations')
#         transports_data = validated_data.pop('transport')
#         accommodationOptions_data = validated_data.pop('accommodationOptions')
#         uniqueness_place_data = validated_data.pop('uniqueness_place')
#         must_see_data = validated_data.pop('must_see')
#         where_to_take_a_picture_data = validated_data.pop('where_to_take_a_picture')
#         cuisines_data = validated_data.pop('cuisines')
#         safes_data = validated_data.pop('safes')
#         entertainments_data = validated_data.pop('entertainments')
#         natural_phenomena_data = validated_data.pop('natural_phenomena')
#         vibes_data = validated_data.pop('vibes')
#         interesting_facts_data = validated_data.pop('interesting_facts')
#         practical_information_data = validated_data.pop('practical_informations')
#         flora_fauna_data = validated_data.pop('flora_fauna')
#
#         place = Place.objects.create(**validated_data)
#         place.category.set(category_data)
#
#         for image_data in images_data:
#             Image.objects.create(place=place, **image_data)
#         for item in locations_data:
#             Location.objects.create(place=place, **item)
#         for transport_data in transports_data:
#             Transport.objects.create(place=place, **transport_data)
#         for accommodationOption_data in accommodationOptions_data:
#             AccommodationOptions.objects.create(place=place, **accommodationOption_data)
#         for uniquenes_place_data in uniqueness_place_data:
#             UniquenessPlace.objects.create(place=place, **uniquenes_place_data)
#         for must_se_data in must_see_data:
#             MustSee.objects.create(place=place, **must_se_data)
#         for where_to_take_a_pictur_data in where_to_take_a_picture_data:
#             WhereToTakeAPicture.objects.create(place=place, **where_to_take_a_pictur_data)
#         for cuisine_data in cuisines_data:
#             Cuisine.objects.create(place=place, **cuisine_data)
#         for safe_data in safes_data:
#             Safe.objects.create(place=place, **safe_data)
#         for entertainment_data in entertainments_data:
#             Entertainment.objects.create(place=place, **entertainment_data)
#         for natural_phenomen_data in natural_phenomena_data:
#             NaturalPhenomena.objects.create(place=place, **natural_phenomen_data)
#         for vibe_data in vibes_data:
#             Vibe.objects.create(place=place, **vibe_data)
#         for interesting_fact_data in interesting_facts_data:
#             InterestingFacts.objects.create(place=place, **interesting_fact_data)
#         for item in practical_information_data:
#             PracticalInformation.objects.create(place=place, **item)
#         for flora_faun_data in flora_fauna_data:
#             FloraFauna.objects.create(place=place, **flora_faun_data)
#         return place


class ClimaticConditionSerializer(ModelSerializer):
    class Meta:
        model = ClimaticCondition
        fields = ('id', 'condition', 'climate', 'description', '__str__')


class ClimaticConditiommSerializer(ModelSerializer):
    class Meta:
        model = ClimaticConditiomm
        fields = '__all__'


class GeographicalFeatureSerializer(ModelSerializer):
    class Meta:
        model = GeographicalFeature
        fields = ('id', 'types_of_ecosystem', 'types_of_ecosystem_description', 'description', '__str__', )


class UserPlaceRelationSerializer(ModelSerializer):
    class Meta:
        model = UserPlaceRelation
        fields = ('id', 'place', 'in_bookmarks', 'rating', 'description_rating')


class GroupSerializer(ModelSerializer):
    places = PlaceListSerializer(many=True, read_only=True)

    class Meta:
        model = Group
        fields = '__all__'




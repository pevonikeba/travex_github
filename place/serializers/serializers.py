from django.contrib.gis.geos import Point
from loguru import logger

from django_countries.serializers import CountryFieldMixin
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from achievement.serializers import AchievementSerializer
from place.models import Place, PlaceImage, ClimaticCondition, \
    FloraFauna, WhereToTakeAPicture, Vibe, MustSee, UniquenessPlace, AccommodationOption, \
    NaturalPhenomena, Entertainment, Cuisine, Safe, Transport, Category, UserPlaceRelation, InterestingFacts, \
    GeographicalFeature, PracticalInformation, TypeTransport, TypeCuisine, CustomUser
from place.serializers.config import location_model_fields
from place.serializers.place_nested import PlaceImageSerializer, TransportSerializer, MustSeeSerializer, \
    AccommodationOptionSerializer, FloraFaunaSerializer, CuisineSerializer, EntertainmentSerializer, \
    NaturalPhenomenaSerializer, SafeSerializer, UniquenessPlaceSerializer, WhereToTakeAPictureSerializer, \
    VibeSerializer, InterestingFactsSerializer, PracticalInformationSerializer


# class FollowingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ('id', 'email', 'username', 'first_name', 'last_name', 'birth', 'bio',
#                   'achievements', 'gender', 'language', 'image',)


class CustomUserPatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'username', 'first_name', 'last_name',
                  'birth', 'bio', 'gender', 'language', 'image', ) + location_model_fields

    def create(self, validated_data):
        logger.info('Here')
        latitude = validated_data.get('latitude')
        longitude = validated_data.get('longitude')
        point = None
        if latitude and longitude:
            point = Point(float(longitude), float(latitude), srid=4326)
        validated_data['point'] = point
        return self.Meta.model.objects.create(**validated_data)


class CustomUserRetrieveSerializer(CustomUserPatchSerializer):  # CustomUserPatchSerializer
    added_places_amount = serializers.SerializerMethodField()
    following_amount = serializers.SerializerMethodField()
    follower_amount = serializers.SerializerMethodField()
    achievement_level_amount = serializers.SerializerMethodField()
    is_follower = serializers.SerializerMethodField()
    is_following = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()
    # followings = FollowingSerializer(many=True, read_only=True)
    # followers = serializers.SerializerMethodField()
    achievements = AchievementSerializer(many=True, required=False, read_only=True, source='first_5_achievements')

    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'username', 'first_name', 'last_name', 'birth', 'bio', 'gender', 'language', 'image',
                  # 'followings', 'followers',
                  'added_places_amount', 'achievements',
                  'following_amount', 'follower_amount', 'is_follower', 'is_following',
                  'achievement_level_amount', ) + location_model_fields

    def get_image(self, user: CustomUser):
        request = self.context.get('request')
        if user.image:
            if request:
                return request.build_absolute_uri(user.image.url)
        else:
            social_auth_img = self.get_social_auth_img(user)
            return social_auth_img or None

    def get_social_auth_img(self, user: CustomUser):
        image = None
        if user.socialaccount_set.exists():
            for social_account in user.socialaccount_set.all():
                brand_name = social_account.get_provider_account().get_brand().get('name')
                if brand_name == 'Google':
                    google_picture = social_account.extra_data['picture']
                    if google_picture:
                        image = google_picture
        return image

    def get_added_places_amount(self, obj: CustomUser):
        return Place.active_objects.filter(writer_user=obj).count()

    def get_is_follower(self, obj):
        request = self.context.get('request')
        if request:
            requested_user: CustomUser = request.user
            if obj.followings.filter(pk=requested_user.pk).exists():
                return True
        return False

    def get_is_following(self, obj):
        request = self.context.get('request')
        if request:
            requested_user: CustomUser = request.user
            if requested_user.followings.filter(pk=obj.pk).exists():
                return True
        return False

        # def get_followers(self, obj):
        #     followers = CustomUser.objects.filter(followings=obj)
        #     response = FollowingSerializer(followers,
        #                                    context={'request': self.context['request']},
        #                                    many=True).data
        #     return response

    def get_following_amount(self, obj: CustomUser):
        return obj.followings.count()

    def get_follower_amount(self, obj: CustomUser):
        return CustomUser.objects.filter(followings=obj).count()

    def get_achievement_level_amount(self, obj: CustomUser):
        achievement_level_amount = 0
        for ach in obj.achievements.all():
            achievement_level_amount += ach.level_increase_to
        return achievement_level_amount


class CustomUserSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    password = serializers.CharField(max_length=255, write_only=True)
    # is_active = serializers.BooleanField()

    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'username', 'image', 'is_active', 'password', 'user',
                  'birth', 'first_name', 'last_name', 'bio',) + location_model_fields

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


class TypeCuisineSerializer(ModelSerializer):
    class Meta:
        model = TypeCuisine
        fields = ('id', 'name',)


class TypeTransportSerializer(ModelSerializer):
    class Meta:
        model = TypeTransport
        fields = ('id', 'name',)


class PlaceSerializer(ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'

    id = serializers.ReadOnlyField()
    writer_user = CustomUserSerializer(default=serializers.CurrentUserDefault())
    categories = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), many=True, required=False)
    place_images = PlaceImageSerializer(many=True, required=False)
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

        place = Place.objects.create(**validated_data)

        if transports_data is not None:
            for item in transports_data:
                Transport.objects.create(place=place, **item)

        if category_data is not None:
            place.category.set(category_data)
        if place_images_data is not None:
            for image_data in place_images_data:
                PlaceImage.objects.create(place=place, **image_data)
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


class ClimaticConditionSerializer(ModelSerializer):
    class Meta:
        model = ClimaticCondition
        fields = ('id', 'condition', 'climate', 'description', '__str__')


class GeographicalFeatureSerializer(ModelSerializer):
    class Meta:
        model = GeographicalFeature
        fields = ('id', 'types_of_ecosystem', 'types_of_ecosystem_description', 'description', '__str__', )


class UserPlaceRelationSerializer(ModelSerializer):
    class Meta:
        model = UserPlaceRelation
        fields = ('id', 'place', 'in_bookmarks', 'rating', 'description_rating')




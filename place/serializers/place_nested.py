from drf_extra_fields.fields import Base64ImageField
from imagekit.cachefiles import ImageCacheFile
from loguru import logger
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from place.models import Transport, PlaceImage, MustSee, AccommodationOption, Category, FloraFauna, Cuisine, \
    Entertainment, NaturalPhenomena, Safe, UniquenessPlace, Vibe, PracticalInformation, InterestingFacts, \
    WhereToTakeAPicture


class CuisineSerializer(ModelSerializer):
    # image = Base64ImageField()  # From DRF Extra Fields
    # name = TypeCuisineSerializer(many=True, required=False, read_only=True)
    # name = serializers.CharField(source='name.type')

    class Meta:
        model = Cuisine
        fields = [field.name for field in model._meta.fields]

    # def create(self, validated_data):
    #     # name_data = validated_data.pop('name')
    #     image = validated_data.pop('image')
    #     data = validated_data.pop('data')
    #
    #     cuisine = Cuisine.objects.create(data=data, image=image)
    #
    #     # cuisine.name.set(name_data)
    #
    #     return cuisine


class EntertainmentSerializer(ModelSerializer):
    class Meta:
        model = Entertainment
        fields = [field.name for field in model._meta.fields]


class NaturalPhenomenaSerializer(ModelSerializer):
    # image = Base64ImageField(Base64ImageField)  # From DRF Extra Fields

    class Meta:
        model = NaturalPhenomena
        fields = [field.name for field in model._meta.fields]


class SafeSerializer(ModelSerializer):
    class Meta:
        model = Safe
        fields = [field.name for field in model._meta.fields]


class UniquenessPlaceSerializer(ModelSerializer):
    class Meta:
        model = UniquenessPlace
        fields = [field.name for field in model._meta.fields]


class VibeSerializer(ModelSerializer):
    class Meta:
        model = Vibe
        fields = [field.name for field in model._meta.fields]


class WhereToTakeAPictureSerializer(ModelSerializer):
    class Meta:
        model = WhereToTakeAPicture
        fields = [field.name for field in model._meta.fields]


class InterestingFactsSerializer(ModelSerializer):
    class Meta:
        model = InterestingFacts
        fields = [field.name for field in model._meta.fields]


class PracticalInformationSerializer(ModelSerializer):
    class Meta:
        model = PracticalInformation
        fields = [field.name for field in model._meta.fields]


class TransportSerializer(serializers.ModelSerializer):
    # image = Base64ImageField(required=False)

    class Meta:
        model = Transport
        fields = [field.name for field in model._meta.fields]
        # fields.append('image')


class PlaceImageSerializer(serializers.ModelSerializer):
    # image = Base64ImageField(required=False)  # From DRF Extra Fields
    image = serializers.SerializerMethodField()

    class Meta:
        model = PlaceImage
        fields = [field.name for field in model._meta.fields]

    def get_image(self, obj: PlaceImage):
        request = self.context.get('request')
        if request:
            return request.build_absolute_uri(obj.image.url)
        return obj.image.url


class MustSeeSerializer(ModelSerializer):
    image = Base64ImageField(required=False)  # From DRF Extra Fields

    class Meta:
        model = MustSee
        fields = [field.name for field in model._meta.fields]
        fields.append('image')


class AccommodationOptionSerializer(ModelSerializer):
    class Meta:
        model = AccommodationOption
        fields = [field.name for field in model._meta.fields]


class CategorySerializer(ModelSerializer):
    # image = Base64ImageField(required=False)  # From DRF Extra Fields

    class Meta:
        model = Category
        fields = [field.name for field in model._meta.fields]
        # fields.append('image')
        fields.append('places')


class FloraFaunaSerializer(ModelSerializer):
    image = Base64ImageField(required=False)  # From DRF Extra Fields

    class Meta:
        model = FloraFauna
        fields = [field.name for field in model._meta.fields]
        fields.append('image')


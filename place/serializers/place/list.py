from loguru import logger
from rest_framework import serializers

from location.serializers import PlaceLocationSerializer
from place.models import Place, CustomUser, PlaceImage
from place.serializers.config import location_model_fields
from place.serializers.place_nested import PlaceImageSerializer
from place.serializers.serializers import CustomUserPatchSerializer, CustomUserRetrieveSerializer


class PlaceListSerializer(serializers.ModelSerializer):
    writer_user = CustomUserRetrieveSerializer()
    place_images = PlaceImageSerializer(many=True)
    is_bookmarked = serializers.SerializerMethodField()
    is_wowed = serializers.SerializerMethodField()
    is_nahed = serializers.SerializerMethodField()
    wows_count = serializers.SerializerMethodField()
    nahs_count = serializers.SerializerMethodField()
    location = PlaceLocationSerializer(read_only=True)

    class Meta:
        model = Place
        fields = ('id', 'name', 'is_bookmarked', 'is_wowed', 'is_nahed',
                  'wows_count', 'nahs_count', 'categories',
                  'description', 'place_images', 'rating',
                  'writer_user', 'home_page', 'location', ) + location_model_fields
        depth = 1

    # def get_is_wowed(self, obj: Place):

    def get_wows_count(self, obj: Place):
        return obj.wowed_users.all().count()

    def get_nahs_count(self, obj: Place):
        return obj.nahed_users.all().count()

    def is_bookmark_like(self, obj, attr_name):
        request = self.context.get('request')
        if request:
            if getattr(obj, attr_name).filter(pk=request.user.id).exists():
                return True
        return False

    def get_is_bookmarked(self, obj: Place):
        return self.is_bookmark_like(obj, 'bookmarked_users')

    def get_is_wowed(self, obj: Place):
        return self.is_bookmark_like(obj, 'wowed_users')

    def get_is_nahed(self, obj:Place):
        return self.is_bookmark_like(obj, 'nahed_users')





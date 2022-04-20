from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

from place.models import Place, Image


class ImageSerializer(serializers.ModelSerializer):
    # path = Base64ImageField()  # From DRF Extra Fields
    class Meta:
        model = Image
        fields = ('id', 'path',)


class PlaceRetrieveSerializer(serializers.ModelSerializer):
    sections = serializers.SerializerMethodField()
    images = ImageSerializer(many=True, required=False)

    class Meta:
        model = Place
        fields = ('id', 'images', 'rating', 'location', 'writer_user', 'sections',)
        # depth = 1

    def get_sections(self, obj):
        return {
            "overview": self.get_overview(obj),
            "perman": "aaaa",
        }

    def get_overview(self, obj):
        return {
            "name": obj.name,
            "description": obj.description,
        }





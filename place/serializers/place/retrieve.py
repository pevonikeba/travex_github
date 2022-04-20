from rest_framework import serializers

from place.models import Place


class PlaceGetRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ('id', 'images', 'rating', 'location', 'writer_user', 'overview', 'sections',)
        # depth = 1
    overview = serializers.SerializerMethodField()
    sections = serializers.SerializerMethodField()

    def get_overview(self, obj):
        return {
            "name": obj.name,
            "description": obj.description,
        }

    def get_sections(self, obj):
        return {
            "perman ->": "name bolmalydygyny aytmaly sen"
        }

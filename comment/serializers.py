from rest_framework import serializers

from comment.models import PlaceComment, SubPlaceComment
from place.serializers.serializers import CustomUserPatchSerializer


class SubPlaceCommentSerializer(serializers.ModelSerializer):
    writer_user = CustomUserPatchSerializer()

    class Meta:
        model = SubPlaceComment
        fields = '__all__'


class PlaceCommentSerializer(serializers.ModelSerializer):
    writer_user = CustomUserPatchSerializer()
    sub_place_comments = SubPlaceCommentSerializer(many=True)

    class Meta:
        model = PlaceComment
        fields = '__all__'
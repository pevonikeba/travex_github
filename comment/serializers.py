from rest_framework import serializers

from comment.models import PlaceComment, SubPlaceComment
from place.serializers.serializers import CustomUserRetrieveSerializer


class SubPlaceCommentSerializer(serializers.ModelSerializer):
    writer_user = CustomUserRetrieveSerializer()

    class Meta:
        model = SubPlaceComment
        fields = '__all__'


class PlaceCommentSerializer(serializers.ModelSerializer):
    writer_user = CustomUserRetrieveSerializer()
    sub_place_comments = SubPlaceCommentSerializer(many=True)

    class Meta:
        model = PlaceComment
        fields = '__all__'
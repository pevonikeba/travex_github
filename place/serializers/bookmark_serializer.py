from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from place.models import Bookmark
from place.serializers.place.list import PlaceListSerializer
from place.serializers.serializers import CustomUserSerializer


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

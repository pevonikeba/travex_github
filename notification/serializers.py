from loguru import logger
from rest_framework import serializers

from notification.models import UserDevice, Notification, Topic
from place.serializers.place.list import PlaceListSerializer
from place.serializers.serializers import CustomUserRetrieveSerializer


class UserDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDevice
        fields = '__all__'


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'


class NotificationSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    main_reference = serializers.SerializerMethodField()
    inline_references = serializers.SerializerMethodField()

    class Meta:
        model = Notification
        fields = ('id', 'title', 'body', 'image', 'created_at', 'main_reference', 'inline_references')

    def place_object(self, place):
        return {
            'type': 'Place',
            'title': place.name,
            'data': PlaceListSerializer(place, context={'request': self.context.get('request')}).data,
        }

    def user_object(self, user):
        return {
            'type': 'User',
            'title': user.username,
            'data': CustomUserRetrieveSerializer(user).data,
        }

    def get_main_reference(self, obj):
        if obj.main_reference:
            place = obj.main_reference.place
            user = obj.main_reference.writer_user
            if place:
                return self.place_object(place)
            elif user:
                return self.user_object(user)
        return None

    def get_inline_references(self, obj):
        if obj.inline_references:
            inline_references_f = []
            for ir in obj.inline_references.all():
                place = ir.place
                user = ir.writer_user
                if place:
                    inline_references_f.append(self.place_object(place))
                elif user:
                    inline_references_f.append(self.user_object(user))
            return inline_references_f
        return None
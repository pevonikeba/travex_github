from rest_framework import serializers

from notification.models import UserDevice, Notification, NotificationSend, Topic
from place.serializers.serializers import CustomUserSerializer


class UserDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDevice
        fields = '__all__'


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'


class NotificationSendSerializer(serializers.ModelSerializer):
    notification = NotificationSerializer()
    topic = TopicSerializer()

    class Meta:
        model = NotificationSend
        fields = ('notification', 'topic', 'created_at', )


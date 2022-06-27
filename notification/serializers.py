from rest_framework import serializers

from notification.models import UserDevice, Notification, Topic

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
    class Meta:
        model = Notification
        fields = ('id', 'title', 'body', 'image', 'created_at', )



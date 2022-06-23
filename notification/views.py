from loguru import logger
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from notification.models import Topic, Notification, UserDevice, NotificationSend
from rest_framework.decorators import action

from place.models import CustomUser
from .fcm_manager import FCMManager
from .serializers import UserDeviceSerializer, NotificationSerializer, NotificationSendSerializer


class UserDeviceViewSet(viewsets.ModelViewSet):
    queryset = UserDevice.objects.all()
    serializer_class = UserDeviceSerializer
    permission_classes = [IsAuthenticated]


class NotificationSendViewSet(mixins.ListModelMixin,
                              viewsets.GenericViewSet):
    serializer_class = NotificationSendSerializer
    queryset = NotificationSend.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        only_my = self.request.query_params.get('only_my')
        if only_my:
            return NotificationSend.objects.filter(users=self.request.user)
        return super(NotificationSendViewSet, self).get_queryset()


class NotificationViewSet(mixins.ListModelMixin,
                          viewsets.GenericViewSet):
    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['POST'])
    def add_or_refresh_user_device(self, request):
        request_user = request.user
        request_device_name: str = request.data.get('device_name')
        request_firebase_token: str = request.data.get('firebase_token')

        user_device = UserDevice.objects.filter(device_name=request_device_name).first()
        if user_device:
            if not user_device.firebase_token == request_firebase_token:
                user_device.firebase_token = request_firebase_token
                user_device.save()
        else:
            UserDevice.objects.create(user=request_user,
                                      device_name=request_device_name,
                                      firebase_token=request_firebase_token)

        return Response({"success": True})

    @action(detail=False)
    def test(self, request):
        tokens = ["dv6uZYBQ794cCEdgTZsJTD:APA91bH8d-UepdmG1jMOt3PruklfPAySJAxnfKSYPNBcbqHo2Rkk-"
                  "LcgXUUzODS8FV7jybib1YIbTT2-4RQBJo7PZ-YoARIZMXhblIWTFl91zF5Qmg3sL4D7dEGLZdPTOTCttZ9HLjzw"]
        # FCMManager.send_token_push("Hi", "This is my next msg", tokens)
        # FCMManager.subscribe_topic("News1", tokens)
        topic_from_db = Topic.objects.filter(topic='News1').first()
        if topic_from_db:
            print(FCMManager.send_topic_push(topic='News1',
                                             title=topic_from_db.title,
                                             body='News1 body'))
        return Response({"success": True})

from django.db import models
from place.models import CustomUser


class UserDevice(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_devices')
    device_name = models.CharField(max_length=255, unique=True, blank=True, null=True)
    firebase_token = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.device_name}'


class Topic(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.title}'


class Notification(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/notifications/', null=True, blank=True)

    def __str__(self):
        return f'{self.title}'


class NotificationSend(models.Model):
    notification = models.ForeignKey(Notification, on_delete=models.PROTECT)
    topic = models.ForeignKey(Topic, on_delete=models.PROTECT, null=True, blank=True)
    users = models.ManyToManyField(CustomUser, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.notification} - {self.topic} - {self.created_at}'

 # IMPRESSION = 'IMP'
 #    OTHER = 'OTH'
 #    NOTIFICATION_TYPES = (
 #        (IMPRESSION, 'Impression'),
 #        (OTHER, 'Other'),
 #    )
 #    type = models.CharField(max_length=5, choices=NOTIFICATION_TYPES)
# user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)

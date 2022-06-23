from django.db import models
from place.models import CustomUser


class UserDevice(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    device_name = models.CharField(max_length=255, unique=True, blank=True, null=True)
    firebase_token = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.device_name}'


class Topic(models.Model):
    title = models.CharField(max_length=255)
    # image = models.ImageField(upload_to='images/notifications/topics/', null=True, blank=True)

    def __str__(self):
        return f'{self.title}'


class Notification(models.Model):
    IMPRESSION = 'IMP'
    OTHER = 'OTH'
    NOTIFICATION_TYPES = (
        (IMPRESSION, 'Impression'),
        (OTHER, 'Other'),
    )
    type = models.CharField(max_length=5, choices=NOTIFICATION_TYPES)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=255)
    body = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # image = models.ImageField(upload_to='images/notifications/', null=True, blank=True)

    def __str__(self):
        return f'{self.title}'

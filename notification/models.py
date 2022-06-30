from django.db import models
from place.models import CustomUser, Place
from place.serializers.place.list import PlaceListSerializer


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


class Reference(models.Model):
    PLACE = 'place'
    USER = 'user'
    TYPE_CHOICES = [
        (PLACE, 'place'),
        (USER, 'user'),
    ]
    type = models.CharField(
        max_length=10,
        choices=TYPE_CHOICES,
        default=PLACE
    )
    title = models.CharField(max_length=255, null=True, blank=True)
    ordering = models.SmallIntegerField(default=0)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, null=True, blank=True)
    writer_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ('ordering',)

    def __str__(self):
        return f'{self.pk}: {self.title}'


class Notification(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/notifications/', null=True, blank=True)
    users = models.ManyToManyField(CustomUser, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    main_reference = models.ForeignKey(Reference, on_delete=models.SET_NULL, related_name='by_main_notifications',
                                       blank=True, null=True)
    inline_references = models.ManyToManyField(Reference, related_name='by_inline_notifications')

    def __str__(self):
        return f'{self.title}: {self.created_at}'




# class PlaceReference(Reference):
#     place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='place_references', blank=True, null=True)
#
#     def get_place_data(self):
#         return PlaceListSerializer(self.place).data
#
#
# class UserReference(Reference):
#     writer_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_references', blank=True, null=True)

    # def get_user_data(self):
    #     return

# class NotificationSend(models.Model):
#     notification = models.ForeignKey(Notification, on_delete=models.PROTECT)
#     topic = models.ForeignKey(Topic, on_delete=models.PROTECT, null=True, blank=True)
#     users = models.ManyToManyField(CustomUser, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f'{self.notification} - {self.topic} - {self.created_at}'

 # IMPRESSION = 'IMP'
 #    OTHER = 'OTH'
 #    NOTIFICATION_TYPES = (
 #        (IMPRESSION, 'Impression'),
 #        (OTHER, 'Other'),
 #    )
 #    type = models.CharField(max_length=5, choices=NOTIFICATION_TYPES)
# user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)

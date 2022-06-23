from django.contrib import admin
from loguru import logger

from notification.fcm_manager import FCMManager
from notification.models import UserDevice, Topic, Notification


@admin.register(UserDevice)
class UserDeviceAdmin(admin.ModelAdmin):
    list_display = ('user', 'device_name')


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    change_form_template = 'admin/notification/topic_change_form.html'

    def response_change(self, request, obj: Topic):
        if "_send_topic_notifications" in request.POST:
            FCMManager.send_topic_push(topic=obj.title,
                                       title=obj.title,
                                       body=obj.body)

        return super(TopicAdmin, self).response_change(request, obj)


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'user')

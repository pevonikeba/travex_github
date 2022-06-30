from django.contrib import admin
from loguru import logger

from notification.fcm_manager import FCMManager
from notification.models import UserDevice, Topic, Notification, Reference


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


@admin.register(Reference)
class ReferenceAdmin(admin.ModelAdmin):
    pass


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', )
    list_display_links = list_display
    filter_horizontal = ('users', )
    change_form_template = 'admin/notification/notification_send_change_form.html'

    def response_change(self, request, obj: Notification):
        if "_send_notification" in request.POST:
            notif_title = obj.title
            notif_body = obj.body
            users = obj.users
            if users.exists():
                # get tokens from user -> user_devices -> firebase_token
                tokens = []
                for user in users.all():
                    for user_device in user.user_devices.all():
                        fb_token = user_device.firebase_token
                        if fb_token:
                            tokens.append(fb_token)
                if tokens:
                    FCMManager.send_token_push(
                        title=notif_title,
                        msg=notif_body,
                        tokens=tokens
                    )

        return super(NotificationAdmin, self).response_change(request, obj)


# @admin.register(NotificationSend)
# class NotificationSendAdmin(admin.ModelAdmin):
#     change_form_template = 'admin/notification/notification_send_change_form.html'
#
#     def response_change(self, request, obj: NotificationSend):
#         if "_send_notification" in request.POST:
#             notification: Notification = obj.notification
#             topic: Topic = obj.topic
#             users = obj.users
#             if topic:
#                 FCMManager.send_topic_push(
#                     topic=topic.title,
#                     title=notification.title,
#                     body=notification.body
#                 )
#             else:
#                 if users.exists():
#                     # get tokens from user -> user_devices -> firebase_token
#                     tokens = []
#                     for user in users.all():
#                         for user_device in user.user_devices.all():
#                             tokens.append(user_device.firebase_token)
#                     if tokens:
#                         FCMManager.send_token_push(
#                             title=notification.title,
#                             msg=notification.body,
#                             tokens=tokens
#                         )
#
#         return super(NotificationSendAdmin, self).response_change(request, obj)

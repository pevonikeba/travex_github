from django.contrib import admin

from notification.models import UserDevice, Topic, Notification


@admin.register(UserDevice)
class UserDeviceAdmin(admin.ModelAdmin):
    pass


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    pass


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'user')

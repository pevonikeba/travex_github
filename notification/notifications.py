from notification.fcm_manager import FCMManager
from notification.models import UserDevice, Notification


def send_impression_notification(user):
    user_devices = UserDevice.objects.filter(user=user)
    if user_devices.exists():
        tokens = []
        for ud in user_devices.all():
            if ud.firebase_token:
                tokens.append(ud.firebase_token)
        if tokens:
            notification_title = 'Impression'
            notification_body = 'You have been wowed by the user'
            notification = Notification.objects.create(
                                        title=notification_title,
                                        body=notification_body)
            notification.users.add(user)
            notification.save()
            FCMManager.send_token_push(notification_title,
                                       notification_body,
                                       tokens)

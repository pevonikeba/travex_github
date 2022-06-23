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
            Notification.objects.create(type=Notification.IMPRESSION,
                                        user=user,
                                        title=notification_title,
                                        body=notification_body)
            FCMManager.send_token_push(notification_title,
                                       notification_body,
                                       tokens)


# def send_topic_notification():
#     FCMManager.send_topic_push()
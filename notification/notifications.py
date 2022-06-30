from loguru import logger

from notification.fcm_manager import FCMManager
from notification.models import UserDevice, Notification, Reference
from place.serializers.place.list import PlaceListSerializer
from place.serializers.place.retrieve import PlaceRetrieveSerializer


class MainReferenceTypes:
    place = 'place'
    user = 'user'


def main_reference(mr_type: str, mr_type_name: str, data):
    return {
        'main_reference': {
            'type': mr_type,
            'title': mr_type_name,
            'data': data
        }
    }


def inline_references(data_list):
    return {
        'inline_references': data_list
    }


def data(data):
    return {
        'data': data
    }


def send_impression_notification(place):
    user = place.writer_user
    user_devices = UserDevice.objects.filter(user=user)
    if user_devices.exists():
        tokens = []
        for ud in user_devices.all():
            if ud.firebase_token:
                tokens.append(ud.firebase_token)
        if tokens:
            notification_title = 'Impression'
            # send by Firebase
            FCMManager.send_token_push(notification_title,
                                       'You have been wowed by the user',
                                       tokens)
            # save in database
            place_main_ref, created = Reference.objects.get_or_create(type=Reference.PLACE,
                                                                      title=place.name,
                                                                      place=place,
                                                                      ordering=1)
            user_inline_ref, created = Reference.objects.get_or_create(type=Reference.USER,
                                                                       title=place.writer_user.username,
                                                                       writer_user=place.writer_user,
                                                                       ordering=0)
            notif = Notification.objects.create(title=notification_title,
                                                body='ref[0] wowed your ref[1]',
                                                main_reference=place_main_ref)
            notif.users.add(place.writer_user)
            notif.inline_references.add(user_inline_ref, place_main_ref)



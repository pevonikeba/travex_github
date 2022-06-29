from loguru import logger

from notification.fcm_manager import FCMManager
from notification.models import UserDevice, Notification
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
    logger.info(place.writer_user)
    place_serializer = PlaceListSerializer(place)
    logger.info(place_serializer.data)

    title = 'Impression'
    body = [
        main_reference(MainReferenceTypes.place, 'Kamchatka', place_serializer.data),
    ]
    logger.info(body)
    # user_devices = UserDevice.objects.filter(user=user)
    # if user_devices.exists():
    #     tokens = []
    #     for ud in user_devices.all():
    #         if ud.firebase_token:
    #             tokens.append(ud.firebase_token)
        # if tokens:
        #     notification_title = 'Impression'
        #     notification_body = 'You have been wowed by the user'
        #     notification = Notification.objects.create(
        #                                 title=notification_title,
        #                                 body=notification_body)
        #     notification.users.add(user)
        #     notification.save()
        #     FCMManager.send_token_push(notification_title,
        #                                notification_body,
        #                                tokens)

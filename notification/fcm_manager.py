import firebase_admin
from firebase_admin import credentials, messaging
from django.conf import settings

from notification.models import Topic, Notification

cred = credentials.Certificate(settings.FIREBASE_CRED_PATH)
firebase_admin.initialize_app(cred)


class FCMManager:
    @staticmethod
    def subscribe_topic(topic: str, tokens) -> bool:
        # response = messaging.subscribe_to_topic(tokens, topic)
        # if response.failure_count > 0:
        #     print(f"Failed to subscribe to topic {topic} due to {list(map(lambda e: e.reason, response.errors))}")
        #     return False
        topic_from_db = Topic.objects.filter(title=topic).first()
        if not topic_from_db:
            Topic.objects.create(title=topic)
        return True

    @staticmethod
    def unsubscribe_topic(topic: str, tokens) -> bool:  # tokens is a list of registration tokens
        response = messaging.unsubscribe_from_topic(tokens, topic)
        if response.failure_count > 0:
            print(f"Failed to subscribe to topic {topic} due to {list(map(lambda e: e.reason, response.errors))}")
            return False
        return True

    # @staticmethod
    # def subscribe_news(tokens):  # tokens is a list of registration tokens
    #     topic = 'news'
    #     response = messaging.subscribe_to_topic(tokens, topic)
    #     if response.failure_count > 0:
    #         print(f"Failed to subscribe to topic {topic} due to {list(map(lambda e: e.reason, response.errors))}")
    #
    # @staticmethod
    # def unsubscribe_news(tokens):  # tokens is a list of registration tokens
    #     topic = 'news'
    #     response = messaging.unsubscribe_from_topic(tokens, topic)
    #     if response.failure_count > 0:
    #         print(f"Failed to subscribe to topic {topic} due to {list(map(lambda e: e.reason, response.errors))}")

    @staticmethod
    def send_topic_push(topic: str, title: str, body: str, image=None):
        message = messaging.Message(
            notification=messaging.Notification(
                title=title,
                body=body,
                image=image
            ),
            topic=topic
        )
        return messaging.send(message)

    @staticmethod
    def send_token_push(title, msg, tokens, dataObject=None): # tokens is a list of registration tokens
        # See documentation on defining a message payload.
        message = messaging.MulticastMessage(
            notification=messaging.Notification(
                title=title,
                body=msg,
            ),
            data=dataObject,
            tokens=tokens,
        )

        # Send a message to the device corresponding to the provided
        # registration token.
        response = messaging.send_multicast(message)
        # Response is a message ID string.
        # print('Successfully sent message:', response)

from loguru import logger

from rest_framework import serializers
from place.models import Transport


class TransportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transport
        fields = ('id', 'type_transport', 'price', 'description', 'comfortable', 'image', 'place',)


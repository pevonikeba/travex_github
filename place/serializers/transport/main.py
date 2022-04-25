from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers
from place.models import Transport


class TransportSerializer(serializers.ModelSerializer):
    image = Base64ImageField(required=False)

    class Meta:
        model = Transport
        fields = ('id', 'type_transport', 'price', 'description', 'comfortable', 'image', 'place',)

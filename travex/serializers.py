from dj_rest_auth.registration.serializers import SocialLoginSerializer
from rest_framework import serializers


class CustomSocialLoginSerializer(SocialLoginSerializer):
    access = serializers.CharField(source='access_token')

    class Meta:
        fields = ('__all__', 'access')


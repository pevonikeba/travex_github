from loguru import logger
from rest_framework.serializers import ModelSerializer

from achievement.models import Achievement
from achievement.models import OwnedAchievement


class AchievementSerializer(ModelSerializer):
    class Meta:
        model = Achievement
        fields = '__all__'


# class OwnedAchievementSerializer(ModelSerializer):
#     class Meta:
#         model = OwnedAchievement
#         fields = '__all__'

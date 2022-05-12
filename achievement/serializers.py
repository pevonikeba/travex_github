from loguru import logger
from rest_framework.serializers import ModelSerializer

from achievement.models import Achievement
from achievement.models import OwnedAchievement


class AchievementSerializer(ModelSerializer):
    class Meta:
        model = Achievement
        fields = '__all__'


class OwnedAchievementSerializer(ModelSerializer):
    class Meta:
        model = OwnedAchievement
        fields = '__all__'

    def create(self, validated_data):
        logger.warning(validated_data)
        # answer, created = OwnedAchievement.objects.update_or_create(
        #     question=validated_data.get('question', None),
        #     defaults={'answer': validated_data.get('answer', None)})
        # return answer
        # return super(OwnedAchievementSerializer, self).create(validated_data)

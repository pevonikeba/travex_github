from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from achievement.models import Achievement
from achievement.serializers import AchievementSerializer


class AchievementViewSet(ReadOnlyModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
    filterset_fields = ['owner', ]

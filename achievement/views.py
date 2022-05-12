from django.db.models import F
from django.shortcuts import render, get_object_or_404
from loguru import logger
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from achievement.models import Achievement, OwnedAchievement
from achievement.serializers import AchievementSerializer, OwnedAchievementSerializer


class AchievementViewSet(ReadOnlyModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer

    @action(detail=True, methods=['post'])
    def add_or_update_own_achievement(self, request, pk=None):
        achievement = get_object_or_404(Achievement, pk=pk)
        # TODO: check if its true

        if achievement.how_to_own == "Get on register":
            pass
        owned_achievement, created = OwnedAchievement.objects.update_or_create(
            writer_user=request.user, achievement=achievement,
            defaults={'level': F('level') + 1}
        )
        serializer = AchievementSerializer(achievement)
        logger.info(serializer.data)
        return Response(serializer.data)
        # answer, created = OwnedAchievement.objects.update_or_create(
        #     question=validated_data.get('question', None),
        #     defaults={'answer': validated_data.get('answer', None)})
        # return answer
        # return super(OwnedAchievementSerializer, self).create(validated_data)

        # place = get_object_or_404(Place, pk=pk)
        # if place.bookmarks.filter(pk=request.user.id).exists():
        #     place.bookmarks.remove(request.user)
        #     place.is_bookmarked = False
        # else:
        #     place.bookmarks.add(request.user)
        #     place.is_bookmarked = True
        # place.save()
        # serializer = PlaceSerializer(place)
        # return Response(serializer.data)

#
# class OwnedAchievementViewSet(ModelViewSet):
#     queryset = OwnedAchievement.objects.all()
#     serializer_class = OwnedAchievementSerializer

    # def create(self, request, *args, **kwargs):
    #     logger.warning(request.data['how_to_own'])
    #     # how_to_own_data = request.data['how_to_own']
    #     # if how_to_own_data == 'on_register':
    #     #     pass
    #
    #     answer, created = self.get_object().objects.update_or_create(
    #         question=validated_data.get('question', None),
    #         defaults={'answer': validated_data.get('answer', None)})
    #     return answer
        #
        # return super(OwnedAchievementViewSet, self).create(request, args, kwargs)

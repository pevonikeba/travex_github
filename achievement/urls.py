from rest_framework.routers import SimpleRouter

from achievement.views import AchievementViewSet

app_name = 'achievement'

router = SimpleRouter()
# root routing "api/achievements"
# router.register(r'owned_achievements', OwnedAchievementViewSet)
router.register('', AchievementViewSet)

urlpatterns = router.urls


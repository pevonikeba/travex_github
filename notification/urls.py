from rest_framework.routers import SimpleRouter

from notification.views import UserDeviceViewSet, NotificationViewSet

app_name = "notification"

router = SimpleRouter()
# root routing "api/notifications/"
router.register(r'devices', UserDeviceViewSet)
router.register('', NotificationViewSet)


urlpatterns = router.urls

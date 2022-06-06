from rest_framework.routers import SimpleRouter

from comment.views import PlaceCommentViewSet, SubPlaceCommentViewSet

app_name = "comment"

router = SimpleRouter()
# root routing "api/comments/"
router.register(r'place_comments', PlaceCommentViewSet)
router.register(r'sub_place_comments', SubPlaceCommentViewSet)


urlpatterns = router.urls

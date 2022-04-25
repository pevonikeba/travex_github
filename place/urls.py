from rest_framework.routers import SimpleRouter

from place.views import PlaceViewSet, GroupViewSet, ClimateViewSet, TypeOfTerrainViewSet, CategoryViewSet, \
    UserPlaceRelationView, TypeTransportViewSet, TypeCuisineViewSet, BookmarkViewSet, \
    TransportViewSet

app_name = "place"

router = SimpleRouter()
# root routing "api/places/"
router.register(r'transports', TransportViewSet)

router.register(r'place_relation', UserPlaceRelationView)
router.register(r'categories', CategoryViewSet)
router.register(r'type_transport', TypeTransportViewSet)
router.register(r'type_cuisine', TypeCuisineViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'bookmarks', BookmarkViewSet)
router.register(r'climates', ClimateViewSet)
router.register(r'terrains', TypeOfTerrainViewSet)
router.register('', PlaceViewSet)

urlpatterns = router.urls

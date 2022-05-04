from rest_framework.routers import SimpleRouter

from place.views import PlaceViewSet, GroupViewSet, ClimateViewSet, TypeOfTerrainViewSet, CategoryViewSet, \
    UserPlaceRelationView, TypeTransportViewSet, TypeCuisineViewSet, BookmarkViewSet, \
    TransportViewSet, PlaceImageViewSet, AccommodationOptionViewSet, MustSeeViewSet, FloraFaunaViewSet

app_name = "place"

router = SimpleRouter()
# root routing "api/places/"
router.register(r"place_images", PlaceImageViewSet)
router.register(r'categories', CategoryViewSet)  # ????????
router.register(r'transports', TransportViewSet)
router.register(r'accommodation_options', AccommodationOptionViewSet)
router.register(r'must_sees', MustSeeViewSet)
router.register(r'flora_faunas', FloraFaunaViewSet)

router.register(r'place_relation', UserPlaceRelationView)
router.register(r'type_transport', TypeTransportViewSet)
router.register(r'type_cuisine', TypeCuisineViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'bookmarks', BookmarkViewSet)
router.register(r'climates', ClimateViewSet)
router.register(r'terrains', TypeOfTerrainViewSet)
router.register('', PlaceViewSet)

urlpatterns = router.urls

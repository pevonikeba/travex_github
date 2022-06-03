from rest_framework.routers import SimpleRouter

from place.views import PlaceViewSet, GroupViewSet, TypeOfTerrainViewSet, CategoryViewSet, \
    UserPlaceRelationView, TypeTransportViewSet, TypeCuisineViewSet, \
    TransportViewSet, PlaceImageViewSet, AccommodationOptionViewSet, MustSeeViewSet, FloraFaunaViewSet, \
    LocationViewSet, ClimaticConditionViewSet, ClimaticConditiommViewSet, MyPlacesViewSet, BookmarkedPlaceViewSet, \
    CuisineViewSet, EntertainmentViewSet, SafeViewSet, UniquenessPlaceViewSet

app_name = "place"

router = SimpleRouter()
# root routing "api/places/"
router.register(r'my_places', MyPlacesViewSet)
router.register(r"place_images", PlaceImageViewSet)
router.register(r'categories', CategoryViewSet)  # ????????
router.register(r'cuisines', CuisineViewSet)
router.register(r'entertainments', EntertainmentViewSet)
router.register(r'safes', SafeViewSet)
router.register(r'uniqueness_places', UniquenessPlaceViewSet)

router.register(r'transports', TransportViewSet)
router.register(r'accommodation_options', AccommodationOptionViewSet)
router.register(r'must_sees', MustSeeViewSet)
router.register(r'flora_faunas', FloraFaunaViewSet)
router.register(r'locations', LocationViewSet)
router.register(r'climatic_condition', ClimaticConditionViewSet)
router.register(r'climatic_conditiomm', ClimaticConditiommViewSet)

router.register(r'place_relation', UserPlaceRelationView)
router.register(r'type_transport', TypeTransportViewSet)
router.register(r'type_cuisine', TypeCuisineViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'bookmarks', BookmarkedPlaceViewSet)
# router.register(r'climates', ClimateViewSet)
router.register(r'terrains', TypeOfTerrainViewSet)
router.register('', PlaceViewSet)

urlpatterns = router.urls


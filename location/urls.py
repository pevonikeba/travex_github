from django.urls import path
from rest_framework.routers import SimpleRouter

from location.views import CityViewSet, DistrictViewSet, CountryViewSet, PostalCodeViewSet, LocationViewSet, \
    HomeAPIView, ChooseViewSet, DetectView, GeoPyChooseView, PlaceLocationViewSet, UserLocationViewSet, \
    NearestPlacesViewSet, ChooseViewSetOld

app_name = "location"

router = SimpleRouter()
# root routing "api/locations/"
router.register('countries', CountryViewSet, basename='countries')
router.register('cities', CityViewSet, basename='cities')
router.register('districts', DistrictViewSet, basename='districts')
router.register('postal_codes', PostalCodeViewSet, basename='postal_codes')
router.register('choose_old', ChooseViewSet, basename='choose_old')
router.register('choose', ChooseViewSetOld, basename='choose')
router.register('places', PlaceLocationViewSet, basename='place')
router.register('users', UserLocationViewSet, basename='user')
router.register('nearest_places', NearestPlacesViewSet, basename='nearest_places')
# router.register('groups', NearestPlaces10kmFirst5, basename='nearest_places_10_km_first_5')
router.register('', LocationViewSet, basename='locations')

urlpatterns = [
    path('detect/', DetectView.as_view()),
    path('test/', GeoPyChooseView.as_view()),
]

urlpatterns += router.urls

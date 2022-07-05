from rest_framework.routers import SimpleRouter

from location.views import CityViewSet, DistrictViewSet, CountryViewSet, PostalCodeViewSet

app_name = "location"

router = SimpleRouter()
# root routing "api/locations/"
router.register('countries', CountryViewSet, basename='countries')
router.register('cities', CityViewSet, basename='cities')
router.register('districts', DistrictViewSet, basename='districts')
router.register('postal_codes', PostalCodeViewSet, basename='postal_codes')


urlpatterns = router.urls

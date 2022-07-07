from django.urls import path
from rest_framework.routers import SimpleRouter

from location.views import CityViewSet, DistrictViewSet, CountryViewSet, PostalCodeViewSet, LocationViewSet, \
    HomeAPIView, TestViewSet

app_name = "location"

router = SimpleRouter()
# root routing "api/locations/"
router.register('countries', CountryViewSet, basename='countries')
router.register('cities', CityViewSet, basename='cities')
router.register('districts', DistrictViewSet, basename='districts')
router.register('postal_codes', PostalCodeViewSet, basename='postal_codes')
router.register('test2', TestViewSet, basename='test2')
router.register('', LocationViewSet, basename='locations')

urlpatterns = [
    path('test/', HomeAPIView.as_view()),

]

urlpatterns = urlpatterns + router.urls

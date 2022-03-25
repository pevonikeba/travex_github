from django.views.generic import ListView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListCreateAPIView
from rest_framework.mixins import UpdateModelMixin
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from place.models import Place, Group, TypeOfTerrain, ClimaticConditions, Category, UserPlaceRelation
from place.serializers import PlaceSerializer, GroupSerializer, TypeOfTerrainSerializer, ClimateSerializer, \
    CategorySerializer, UserPlaceRelationSerializer

class PlaceAPIListPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 10000

class PlaceViewSet(ModelViewSet, ListView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['category']
    search_fields = ['name', 'nickname']
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = PlaceAPIListPagination

class UserPlaceRelationView(UpdateModelMixin, GenericViewSet):
    queryset = UserPlaceRelation.objects.all()
    serializer_class = UserPlaceRelationSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'place'

    def get_object(self):
        obj, created = UserPlaceRelation.objects.get_or_create(user=self.request.user, place_id=self.kwargs['place'])
        return obj


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ClimateViewSet(ModelViewSet, ListView):
    queryset = ClimaticConditions.objects.all()
    serializer_class = ClimateSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class TypeOfTerrainViewSet(ModelViewSet):
    queryset = TypeOfTerrain.objects.all()
    serializer_class = TypeOfTerrainSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

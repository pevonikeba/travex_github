from django.views.generic import ListView
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from place.models import Place, Group, TypeOfTerrain, ClimaticConditions
from place.serializers import PlaceSerializer, GroupSerializer, TypeOfTerrainSerializer, ClimateSerializer


class PlaceViewSet(ModelViewSet, ListView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class TypeOfTerrainViewSet(ModelViewSet):
    queryset = TypeOfTerrain.objects.all()
    serializer_class = TypeOfTerrainSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ClimateViewSet(ModelViewSet):
    queryset = ClimaticConditions.objects.all()
    serializer_class = ClimateSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

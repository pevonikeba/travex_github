from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from place.models import Place, Group, Transport, AccommodationOptions, UniquenessPlace, MustSee, WhereToTakeAPicture
from place.serializers import PlaceSerializer, GroupSerializer, TransportSerializer, AccommodationOptionsSerializer, \
    MustSeeSerializer, WhereToTakeAPictureSerializer


class PlaceViewSet(ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class TransportiewSet(ModelViewSet):
    queryset = Transport.objects.all()
    serializer_class = TransportSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class AccommodationOptionsViewSet(ModelViewSet):
    queryset = AccommodationOptions.objects.all()
    serializer_class = AccommodationOptionsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class UniquenessPlaceViewSet(ModelViewSet):
    queryset = UniquenessPlace.objects.all()
    serializer_class = AccommodationOptionsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class MustSeeViewSet(ModelViewSet):
    queryset = MustSee.objects.all()
    serializer_class = MustSeeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class WhereToTakeAPictureViewSet(ModelViewSet):
    queryset = WhereToTakeAPicture.objects.all()
    serializer_class = WhereToTakeAPictureSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from place.models import Place, Groups
from place.serializers import PlaceSerializer, GroupSerializer


class PlaceViewSet(ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    # permission_classes = [IsAuthenticated]

class GroupViewSet(ModelViewSet):
    queryset = Groups.objects.all()
    serializer_class = GroupSerializer
    # permission_classes = [IsAuthenticated]

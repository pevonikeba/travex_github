from rest_framework import viewsets
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser

from comment.models import PlaceComment, SubPlaceComment
from comment.serializers import PlaceCommentSerializer, SubPlaceCommentSerializer
from rest_framework.permissions import IsAuthenticated


class SubPlaceCommentViewSet(viewsets.ModelViewSet):
    # parser_classes = [JSONParser, FormParser, MultiPartParser, ]
    serializer_class = SubPlaceCommentSerializer
    queryset = SubPlaceComment.objects.all()
    filterset_fields = ['place_comment', ]


class PlaceCommentViewSet(viewsets.ModelViewSet):
    # parser_classes = [JSONParser, FormParser, MultiPartParser, ]
    serializer_class = PlaceCommentSerializer
    queryset = PlaceComment.objects.all()
    filterset_fields = ['place', ]
    permission_classes = [IsAuthenticated]


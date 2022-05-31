import json

# from rest_framework_simplejwt.locale import

import requests
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from django_filters.rest_framework import DjangoFilterBackend
from djoser.views import UserViewSet
from rest_framework import status, exceptions, filters, mixins, viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import UpdateModelMixin
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.status import HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet, ReadOnlyModelViewSet

from place.models import Place, Group, ClimaticCondition, Category, UserPlaceRelation, GeographicalFeature, \
    TypeTransport, TypeCuisine, CustomUser, Transport, PlaceImage, AccommodationOption, MustSee, FloraFauna, \
    Location, Bookmark, ClimaticConditiomm
from place.serializers.place.create import PlaceCreateSerializer
from place.serializers.place.list import PlaceListSerializer
from place.serializers.place.retrieve import PlaceRetrieveSerializer, PlaceOnAddDeleteBookmarkLikeSerializer
from place.serializers.place_plus import get_plus_place
from place.serializers.serializers import PlaceSerializer, GroupSerializer, ClimaticConditionSerializer, \
    UserPlaceRelationSerializer, GeographicalFeatureSerializer, \
    TypeTransportSerializer, TypeCuisineSerializer, CustomUserSerializer, \
    LocationSerializer, BookmarkSerializer, ClimaticConditiommSerializer, CustomUserImageSerializer, \
    CustomUserPatchSerializer
from place.serializers.place_nested import TransportSerializer, PlaceImageSerializer, MustSeeSerializer, \
    AccommodationOptionSerializer, CategorySerializer, FloraFaunaSerializer


from rest_framework.parsers import JSONParser, FormParser, MultiPartParser

from place.utils.utils import StandardResultsSetPagination, get_social_account_brands, SocialAccountError, \
    check_has_social_account_error_msg
from django.conf import settings
# from rest_auth.registration.views import SocialLoginView
from loguru import logger

#
# class TokenRefreshView(TokenViewBase):
#     """
#         Renew tokens (access and refresh) with new expire time based on specific user's access token.
#     """
#     serializer_class = TokenRefreshLifetimeSerializer


# class CustomRenderer(JSONRenderer):
#     def render(self, data, accepted_media_type=None, renderer_context=None):
#         response_content = {}
#         if type(data) is dict and data['custom_error'] == True:
#             response_content['success'] = False
#             response_content['error'] = data['code'] or 'unknown_error'
#         else:
#             response_content['success'] = True
#             response_content['data'] = data
#         return super(CustomRenderer, self).render(response_content, accepted_media_type, renderer_context)


# class PlaceAPIListPagination(PageNumberPagination):
#     page_size = 10
#     page_size_query_param = 'page_size'
#     max_page_size = 10000


# from django.contrib.gis.geos import Point

# from geopy.geocoders import Nominatim
# from OSMPythonTools.nominatim import Nominatim


# geolocator = Nominatim(user_agent="attaplace")


from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def check_version(request):
    res = {
        "WORKING": {
            "status": "WORKING",
            "message": "Sorry, we are working",
        },
        "UPDATE": {
            "status": "UPDATE",
            "message": "It is necessary to update the app",
        },
        "GOOD": {
            "status": "GOOD",
            "message": "You have a valid version",
        }
    }
    if settings._VERSION.get('WORKING'):
        return Response(res['WORKING'])

    version = request.query_params.get('version')
    if version not in settings._VERSION.get('WHITELIST'):
        return Response(res['UPDATE'])
    return Response(res['GOOD'])


class DestroyWithPayloadMixin(object):
    def destroy(self, *args, **kwargs):
        serializer = self.get_serializer(self.get_object())
        super().destroy(*args, **kwargs)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PlaceNestedViewSet(DestroyWithPayloadMixin, ModelViewSet):
    """Common ViewSet for place nested models"""
    parser_classes = [JSONParser, FormParser, MultiPartParser, ]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['place', ]
    permission_classes = [IsAuthenticatedOrReadOnly]


class PlaceImageViewSet(PlaceNestedViewSet):
    queryset = PlaceImage.objects.all()
    serializer_class = PlaceImageSerializer


class TransportViewSet(PlaceNestedViewSet):
    queryset = Transport.objects.all()
    serializer_class = TransportSerializer


class AccommodationOptionViewSet(PlaceNestedViewSet):
    queryset = AccommodationOption.objects.all()
    serializer_class = AccommodationOptionSerializer


class MustSeeViewSet(PlaceNestedViewSet):
    queryset = MustSee.objects.all()
    serializer_class = MustSeeSerializer


class FloraFaunaViewSet(PlaceNestedViewSet):
    queryset = FloraFauna.objects.all()
    serializer_class = FloraFaunaSerializer


class ClimaticConditionViewSet(PlaceNestedViewSet):
    queryset = ClimaticCondition.objects.all()
    serializer_class = ClimaticConditionSerializer


class ClimaticConditiommViewSet(PlaceNestedViewSet):
    queryset = ClimaticConditiomm.objects.all()
    serializer_class = ClimaticConditiommSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, ]
    # filterset_fields = ['home_page', 'writer_user', ]
    search_fields = ['name', ]


class PlaceViewSet(DestroyWithPayloadMixin, ModelViewSet):
    parser_classes = [JSONParser, FormParser, MultiPartParser, ]
    queryset = Place.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, ]
    filterset_fields = ['home_page', 'writer_user', 'categories']
    search_fields = ['name', 'locations__country', 'locations__city', ]
    default_serializer_class = PlaceSerializer
    serializer_classes = {
        'list': PlaceListSerializer,
        'retrieve': PlaceRetrieveSerializer,
        'create': PlaceCreateSerializer,
        # 'put': PlaceCreateSerializer,
        # 'patch': PlacePatchSerializer,
    }
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    def get_queryset(self):
        queryset = Place.objects.all()
        if self.action == 'list':
            queryset = queryset.filter(is_active=True)
            # TODO: if in query params has 'category' exec it, but change query param to 'categories' later on mob.app
            category = self.request.query_params.get('category')
            if category is not None:
                queryset = queryset.filter(categories=category)
            return queryset
        return queryset


    @action(detail=False, methods=["get"])
    def plus_place(self, request):
        return Response(get_plus_place())

    @action(detail=True, methods=['get'])
    def plus_place_get(self, request, pk=None):
        queryset = Place.objects.all()
        place = get_object_or_404(queryset, pk=pk)
        serializer = PlaceSerializer(place)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def add_or_delete_bookmark(self, request, pk=None):
        place = get_object_or_404(Place, pk=pk)
        if place.bookmarked_users.filter(pk=request.user.id).exists():
            place.bookmarked_users.remove(request.user)
            is_bookmarked = False
        else:
            place.bookmarked_users.add(request.user)
            is_bookmarked = True

        place.save()
        # logger.info(place.bookmarked_users.count())
        return Response({'is_bookmarked': is_bookmarked})

    @action(detail=True, methods=['post'])
    def add_or_delete_wow(self, request, pk=None):
        place = get_object_or_404(Place, pk=pk)
        if place.wowed_users.filter(pk=request.user.id).exists():
            place.wowed_users.remove(request.user)
            is_wowed = False
        else:
            place.wowed_users.add(request.user)
            is_wowed = True
            if place.nahed_users.filter(pk=request.user.id).exists():
                place.nahed_users.remove(request.user)

        return Response({
            'is_wowed': is_wowed,
            'is_nahed': False,
        })

    @action(detail=True, methods=['post'])
    def add_or_delete_nah(self, request, pk=None):
        place = get_object_or_404(Place, pk=pk)
        if place.nahed_users.filter(pk=request.user.id).exists():
            place.nahed_users.remove(request.user)
            is_nahed = False
        else:
            place.nahed_users.add(request.user)
            is_nahed = True
            if place.wowed_users.filter(pk=request.user.id).exists():
                place.wowed_users.remove(request.user)

        return Response({
            'is_nahed': is_nahed,
            'is_wowed': False,
        })


class MyPlacesViewSet(mixins.ListModelMixin,
                      GenericViewSet):
    """Only for own writer user places"""
    queryset = Place.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, ]
    filterset_fields = ['home_page', 'writer_user', 'categories']
    search_fields = ['name', 'locations__country', 'locations__city', ]
    serializer_class = PlaceListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Place.objects.filter(is_active=True, writer_user=self.request.user)


def get_location(lat, lon):
    url = f'https://nominatim.openstreetmap.org/reverse?lat={lat}&lon={lon}&format=json&accept-language=en&zoom=10'
    try:
        result = requests.get(url=url)
        result_json = result.json()
        logger.warning(result_json)
        return result_json
    except:
        return None


class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if serializer.is_valid():
            latitude = serializer.validated_data["latitude"]
            longitude = serializer.validated_data['longitude']
            logger.warning(latitude)
            logger.warning(longitude)
            location = get_location(latitude, longitude)
            if location:
                logger.info(location)
                address = location.get("address")
                logger.warning(address)
                # extra_data = serializer.data
                if address:
                    country = address.get("country")
                    state = address.get("state")
                    county = address.get("county")
                    city = address.get("city")
                    # TODO: get continent
                    serializer.save(country=country, city=city, state=state, county=county)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return super(LocationViewSet, self).create(request, args, kwargs)


class UserPlaceRelationView(UpdateModelMixin, GenericViewSet):
    queryset = UserPlaceRelation.objects.all()
    serializer_class = UserPlaceRelationSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    # renderer_classes = [CustomRenderer, BrowsableAPIRenderer]
    lookup_field = 'place'

    def get_object(self):
        obj, created = UserPlaceRelation.objects.get_or_create(user=self.request.user, place_id=self.kwargs['place'])
        return obj


class BookmarkedPlaceViewSet(mixins.ListModelMixin,
                      viewsets.GenericViewSet):

    queryset = Place.objects.all()
    serializer_class = PlaceListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Place.objects.filter(bookmarked_users=self.request.user)


class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    # renderer_classes = [CustomRenderer, BrowsableAPIRenderer]


# class ClimateViewSet(ModelViewSet, ListView):
#     queryset = ClimaticCondition.objects.all()
#     serializer_class = ClimaticConditionSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]
    # renderer_classes = [CustomRenderer, BrowsableAPIRenderer]


class TypeOfTerrainViewSet(ModelViewSet):
    queryset = GeographicalFeature.objects.all()
    serializer_class = GeographicalFeatureSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    # renderer_classes = [CustomRenderer, BrowsableAPIRenderer]


class TypeTransportViewSet(ModelViewSet):
    queryset = TypeTransport.objects.all()
    serializer_class = TypeTransportSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    # renderer_classes = [CustomRenderer, BrowsableAPIRenderer]


class TypeCuisineViewSet(ModelViewSet):
    queryset = TypeCuisine.objects.all()
    serializer_class = TypeCuisineSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    # renderer_classes = [CustomRenderer, BrowsableAPIRenderer]


# class CsrfExemptSessionAuthentication(SessionAuthentication):
#     def enforce_csrf(self, request):
#         return None


# class CustomUserListCreateView(ListCreateAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = CustomUserSerializer
#     filter_backends = [DjangoFilterBackend, SearchFilter]
#     filterset_fields = ['email']
#
#     # renderer_classes = [CustomRenderer, BrowsableAPIRenderer]
#     # permission_classes = [IsAuthenticated]
#     # permission_classes = [DjangoModelPermissions]
#     # permission_classes = [CsrfExemptSessionAuthentication]
#
#     def perform_create(self, serializer):
#         # user = self.request.user
#         # serializer.save(user=user)
#
#         serializer.save()


class CustomUserViewSetFromDjoser(UserViewSet):
    def create(self, request, *args, **kwargs):
        try:
            user = CustomUser.objects.get(email=request.data['email'])
            social_account_brands = get_social_account_brands(user)
            if check_has_social_account_error_msg(social_account_brands):
                # raise Exception("aaa")
                return Response(social_account_brands, status=HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS)
            if not user.is_active:
                user.delete()
        except:
            pass
        return super().create(request, *args, **kwargs)


class CustomUserViewSet(mixins.UpdateModelMixin,
                        viewsets.GenericViewSet):
    parser_classes = [JSONParser, FormParser, MultiPartParser, ]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserPatchSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['patch'])
    def add_or_delete_subscriber(self, request, pk=None):
        user: CustomUser = request.user
        subscriber: CustomUser = CustomUser.objects.filter(pk=pk).first()
        if subscriber:
            if user.subscribed_users.filter(pk=pk).exists():
                user.subscribed_users.remove(subscriber)
                return Response({'unsubscribed_from': subscriber.email})
            else:
                user.subscribed_users.add(subscriber)
                return Response({'subscribed_to': subscriber.email})

# class CustomUserDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = CustomUserSerializer
#     permission_classes = [IsAuthenticated]
    # renderer_classes = [CustomRenderer, BrowsableAPIRenderer]


# class ActivateUser(UserViewSet):
#     def get_serializer(self, *args, **kwargs):
#         serializer_class = self.get_serializer_class()
#         kwargs.setdefault('context', self.get_serializer_context())
#
#         # this line is the only change from the base implementation.
#         kwargs['data'] = {"uid": self.kwargs['uid'], "token": self.kwargs['token']}
#
#         return serializer_class(*args, **kwargs)
#
#     @action(["post"], detail=False)
#     def activation(self, request, uid, token, *args, **kwargs):
#         super().activation(request, *args, **kwargs)
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class UserActivationView(APIView):
#     def get (self, request, uid, token):
#         protocol = 'https://' if request.is_secure() else 'http://'
#         web_url = protocol + request.get_host()
#         post_url = web_url + "/auth/users/activate/"
#         post_data = {'uid': uid, 'token': token}
#         result = requests.post(post_url, data=post_data)
#         content = result.text
#         return Response(content)
#
#
# class ActivateUser(GenericAPIView):
#
#     def get(self, request, uid, token, format = None):
#         payload = {'uid': uid, 'token': token}
#
#         url = "http://localhost:8000/api/v1/auth/users/activation/"
#         response = requests.post(url, data=payload)
#
#         if response.status_code == 204:
#             return Response({}, response.status_code)
#         else:
#             return Response(response.json())

# @api_view(["GET"])
# @permission_classes([permissions.AllowAny])
# def request_user_activation(request, uid, token):
#     """
#     Intermediate view to activate a user's email.
#     """
#     print("request_user_activation zdes")
#     post_url = "http://127.0.0.1:8000/djoser_auth/users/activation/"
#     post_data = {"uid": uid, "token": token}
#     result = requests.post(post_url, data=post_data)
#     content = result.text
#     return Response(content)

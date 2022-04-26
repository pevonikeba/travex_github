import json

# from rest_framework_simplejwt.locale import
import djoser.urls.jwt

import requests
from dj_rest_auth.registration.serializers import SocialLoginSerializer
from dj_rest_auth.registration.views import SocialLoginView
from django.views.generic import ListView
from django_filters.rest_framework import DjangoFilterBackend
from djoser.views import UserViewSet
from rest_framework import viewsets, status, permissions
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.exceptions import ErrorDetail
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView, DestroyAPIView
from rest_framework.mixins import UpdateModelMixin
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, DjangoModelPermissionsOrAnonReadOnly, \
    DjangoModelPermissions, AllowAny
from rest_framework.utils.serializer_helpers import ReturnList
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from place.models import Place, Group, ClimaticCondition, Category, UserPlaceRelation, GeographicalFeature, \
    TypeTransport, TypeCuisine, CustomUser, Bookmark, Transport, Image
from place.serializers.place.create import PlaceCreateSerializer
from place.serializers.place.list import PlaceListSerializer
from place.serializers.place.retrieve import PlaceRetrieveSerializer
from place.serializers.plus_place import get_plus_place
from place.serializers.serializers import PlaceSerializer, GroupSerializer, ClimateSerializer, \
    CategorySerializer, UserPlaceRelationSerializer, GeographicalFeatureSerializer, \
    TypeTransportSerializer, TypeCuisineSerializer, CustomUserSerializer, BookmarkSerializer, \
    CustomSocialLoginSerializer, ImageSerializer
from place.serializers.transport.main import TransportSerializer

from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from allauth.socialaccount.providers.apple.views import AppleOAuth2Adapter, AppleOAuth2Client, AppleProvider
# from rest_auth.registration.views import SocialLoginView


from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer

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
# geolocator = Nominatim(user_agent="location")

class ImageViewSet(ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class TransportViewSet(ModelViewSet):
    queryset = Transport.objects.all()
    serializer_class = TransportSerializer


class PlaceViewSet(ModelViewSet):
    queryset = Place.objects.all()
    default_serializer_class = PlaceSerializer
    serializer_classes = {
        'list': PlaceListSerializer,
        'retrieve': PlaceRetrieveSerializer,
        'create': PlaceCreateSerializer,
        # 'put': PlaceCreateSerializer,
        # 'patch': PlaceCreateSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    @action(detail=False, methods=["get"])
    def plus_place(self, request):
        return Response(get_plus_place())

    @action(detail=False, methods=["get"])
    def test(self, request):
        queryset = Place.objects.all()
        serializer = PlaceSerializer(queryset, many=True)
        return Response(serializer.data)


class UserPlaceRelationView(UpdateModelMixin, GenericViewSet):
    queryset = UserPlaceRelation.objects.all()
    serializer_class = UserPlaceRelationSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    # renderer_classes = [CustomRenderer, BrowsableAPIRenderer]
    lookup_field = 'place'

    def get_object(self):
        obj, created = UserPlaceRelation.objects.get_or_create(user=self.request.user, place_id=self.kwargs['place'])
        return obj


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    # renderer_classes = [CustomRenderer, BrowsableAPIRenderer]


class BookmarkViewSet(ModelViewSet):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # renderer_classes = [CustomRenderer, BrowsableAPIRenderer]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    # renderer_classes = [CustomRenderer, BrowsableAPIRenderer]


class ClimateViewSet(ModelViewSet, ListView):
    queryset = ClimaticCondition.objects.all()
    serializer_class = ClimateSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
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


class AppleLogin(SocialLoginView):
    adapter_class = AppleOAuth2Adapter
    callback_url = 'https://anycallbackurlhere'
    client_class = AppleOAuth2Client


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client
    serializer_class = CustomSocialLoginSerializer

    # serializer_class = SocialLoginSerializer
    # renderer_classes = [CustomRenderer, BrowsableAPIRenderer]

    def process_login(self):
        self.user.is_active = True
        self.user.save()
        super().process_login()


# class CsrfExemptSessionAuthentication(SessionAuthentication):
#     def enforce_csrf(self, request):
#         return None


class CustomUserListCreateView(ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['email']

    # renderer_classes = [CustomRenderer, BrowsableAPIRenderer]
    # permission_classes = [IsAuthenticated]
    # permission_classes = [DjangoModelPermissions]
    # permission_classes = [CsrfExemptSessionAuthentication]

    def perform_create(self, serializer):
        # user = self.request.user
        # serializer.save(user=user)

        serializer.save()


class CustomUserView(UserViewSet):

    def create(self, request, *args, **kwargs):

        try:
            user = CustomUser.objects.get(email=request.data['email'])
            if not user.is_active:
                user.delete()
        except:
            pass
        return super().create(request, *args, **kwargs)


class CustomUserDetailView(RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]
    # renderer_classes = [CustomRenderer, BrowsableAPIRenderer]


from rest_framework.response import Response


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

class ActivateUserEmail(APIView):
    def get(self, request, uid, token):
        protocol = 'https://' if request.is_secure() else 'http://'
        web_url = protocol + request.get_host()
        post_url = web_url + "/auth/users/activation/"
        post_data = json.dumps({'uid': uid, 'token': token})
        result = requests.post(post_url, data=post_data, headers={'Content-Type': 'application/json'})
        message = result.text
        if message == '':
            message = "Pereydite w prelozheniye Attaplace"

        return Response(message)

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

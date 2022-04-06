import json

import requests
from dj_rest_auth.registration.serializers import SocialLoginSerializer
from dj_rest_auth.registration.views import SocialLoginView
from django.views.generic import ListView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status, permissions
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView
from rest_framework.mixins import UpdateModelMixin
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, DjangoModelPermissionsOrAnonReadOnly, \
    DjangoModelPermissions
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from place.models import Place, Group, ClimaticConditions, Category, UserPlaceRelation, GeographicalFeature, \
    TypeTransport, TypeCuisine, CustomUser, Bookmark
from place.serializers import PlaceSerializer, GroupSerializer, ClimateSerializer, \
    CategorySerializer, UserPlaceRelationSerializer, GeographicalFeatureSerializer, \
    TypeTransportSerializer, TypeCuisineSerializer, CustomUserSerializer, BookmarkSerializer

from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
# from rest_auth.registration.views import SocialLoginView


class PlaceAPIListPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 10000

class PlaceViewSet(ModelViewSet, ListView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['category', 'home_page']
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


class BookmarkViewSet(ModelViewSet):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
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
    queryset = GeographicalFeature.objects.all()
    serializer_class = GeographicalFeatureSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class TypeTransportViewSet(ModelViewSet):
    queryset = TypeTransport.objects.all()
    serializer_class = TypeTransportSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class TypeCuisineViewSet(ModelViewSet):
    queryset = TypeCuisine.objects.all()
    serializer_class = TypeCuisineSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]





class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client
    serializer_class = SocialLoginSerializer


# class CsrfExemptSessionAuthentication(SessionAuthentication):
#     def enforce_csrf(self, request):
#         return None

class CustomUserListCreateView(ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    # permission_classes = [IsAuthenticated]
    # permission_classes = [DjangoModelPermissions]
    # permission_classes = [CsrfExemptSessionAuthentication]

    def perform_create(self, serializer):
        # user = self.request.user
        # serializer.save(user=user)

        serializer.save()

class CustomUserDetailView(RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]


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
    def get (self, request, uid, token):
        protocol = 'https://' if request.is_secure() else 'http://'
        web_url = protocol + request.get_host()
        post_url = web_url + "/auth/users/activation/"
        post_data = json.dumps({'uid': uid, 'token': token})
        result = requests.post(post_url, data=post_data, headers={'Content-Type': 'application/json'})
        message = result.text

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
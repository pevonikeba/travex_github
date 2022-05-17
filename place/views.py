import json

# from rest_framework_simplejwt.locale import

import requests
from dj_rest_auth.registration.views import SocialLoginView
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView
from django_filters.rest_framework import DjangoFilterBackend
from djoser.views import UserViewSet
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import UpdateModelMixin
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet, ReadOnlyModelViewSet

from place.models import Place, Group, ClimaticCondition, Category, UserPlaceRelation, GeographicalFeature, \
    TypeTransport, TypeCuisine, CustomUser, Transport, PlaceImage, AccommodationOption, MustSee, FloraFauna, \
    Location, Bookmark
from place.serializers.place.create import PlaceCreateSerializer
from place.serializers.place.list import PlaceListSerializer
from place.serializers.place.retrieve import PlaceRetrieveSerializer, PlaceOnAddDeleteBookmarkSerializer
from place.serializers.place_plus import get_plus_place
from place.serializers.serializers import PlaceSerializer, GroupSerializer, ClimateSerializer, \
    UserPlaceRelationSerializer, GeographicalFeatureSerializer, \
    TypeTransportSerializer, TypeCuisineSerializer, CustomUserSerializer, \
    CustomSocialLoginSerializer, LocationSerializer, BookmarkSerializer
from place.serializers.place_nested import TransportSerializer, PlaceImageSerializer, MustSeeSerializer, \
    AccommodationOptionSerializer, CategorySerializer, FloraFaunaSerializer

from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from allauth.socialaccount.providers.apple.views import AppleOAuth2Adapter, AppleOAuth2Client
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser

from place.utils.utils import StandardResultsSetPagination
from django.conf import settings
# from rest_auth.registration.views import SocialLoginView
from loguru import logger

# from rest_framework_simplejwt.views import TokenViewBase
# from place.serializers.serializers import TokenObtainLifetimeSerializer, TokenRefreshLifetimeSerializer


# class TokenObtainPairView(TokenViewBase):
#     """
#         Return JWT tokens (access and refresh) for specific user based on username and password.
#     """
#     serializer_class = TokenObtainLifetimeSerializer
#
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


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class PlaceViewSet(DestroyWithPayloadMixin, ModelViewSet):
    parser_classes = [JSONParser, FormParser, MultiPartParser, ]
    queryset = Place.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['home_page', 'writer_user', ]
    default_serializer_class = PlaceSerializer
    serializer_classes = {
        'list': PlaceListSerializer,
        'retrieve': PlaceRetrieveSerializer,
        'create': PlaceCreateSerializer,
        # 'put': PlaceCreateSerializer,
        # 'patch': PlacePatchSerializer,
    }
    # pagination_class = StandardResultsSetPagination
    permission_classes = [IsAuthenticatedOrReadOnly]

    # def update(self, request, *args, **kwargs):
    #     super().update(request, *args, **kwargs)
    #     serializer = PlaceRetrieveSerializer(self.get_object())
    #     return Response(serializer.data, status=status.HTTP_200_OK)

    def get_queryset(self):
        if self.action == 'list':
            return Place.objects.filter(is_active=True)
        return Place.objects.all()

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

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
            place.is_bookmarked = False
        else:
            place.bookmarked_users.add(request.user)
            place.is_bookmarked = True
        place.save()
        serializer = PlaceOnAddDeleteBookmarkSerializer(place)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def my_places(self, request):
        # get all places (active or not)
        queryset = Place.objects.filter(writer_user=request.user)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = PlaceListSerializer(queryset, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def bookmarks(self, request):
        queryset = self.filter_queryset(self.get_queryset()).filter(bookmarked_users=request.user)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = PlaceListSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


def eula(request):
    html = '''
    </body></html>
        <h2>End-User License Agreement (EULA) of Attaplace</h2>

<p>This End-User License Agreement ("EULA") is a legal agreement between you and Attaplace</p>

<p>This EULA agreement governs your acquisition and use of our Attaplace software ("Software") directly from Attaplace or indirectly through a Attaplace authorized reseller or distributor (a "Reseller").</p>

<p>Please read this EULA agreement carefully before completing the installation process and using the Attaplace software. It provides a license to use the Attaplace software and contains warranty information and liability disclaimers.</p>

<p>If you register for a free trial of the Attaplace software, this EULA agreement will also govern that trial. By clicking "accept" or installing and/or using the Attaplace software, you are confirming your acceptance of the Software and agreeing to become bound by the terms of this EULA agreement.</p>

<p>If you are entering into this EULA agreement on behalf of a company or other legal entity, you represent that you have the authority to bind such entity and its affiliates to these terms and conditions. If you do not have such authority or if you do not agree with the terms and conditions of this EULA agreement, do not install or use the Software, and you must not accept this EULA agreement.</p>

<p>This EULA agreement shall apply only to the Software supplied by Attaplace herewith regardless of whether other software is referred to or described herein. The terms also apply to any Attaplace updates, supplements, Internet-based services, and support services for the Software, unless other terms accompany those items on delivery. If so, those terms apply.</p>

<h3>License Grant</h3>

<p>Attaplace hereby grants you a personal, non-transferable, non-exclusive licence to use the Attaplace software on your devices in accordance with the terms of this EULA agreement.</p>

<p>You are permitted to load the Attaplace software (for example a PC, laptop, mobile or tablet) under your control. You are responsible for ensuring your device meets the minimum requirements of the Attaplace software.</p>

<p>You are not permitted to:</p>

<ul>
<li>Edit, alter, modify, adapt, translate or otherwise change the whole or any part of the Software nor permit the whole or any part of the Software to be combined with or become incorporated in any other software, nor decompile, disassemble or reverse engineer the Software or attempt to do any such things</li>
<li>Reproduce, copy, distribute, resell or otherwise use the Software for any commercial purpose</li>
<li>Allow any third party to use the Software on behalf of or for the benefit of any third party</li>
<li>Use the Software in any way which breaches any applicable local, national or international law</li>
<li>Use the Software for any purpose that Attaplace considers is a breach of this EULA agreement</li>
<li>Post illegal products or services, tobacco and related products, drugs and drug related products, spyware or malware, and prohibited financial products and services.</li>
<li>Post abusive, illegal, sexual, or racist content. Users will be responsible for the actions taken within the application.</li>
<li>To post pictures of your children as we are not taking responsibilities to where the content will be published.</li>

</ul>

<h3>Intellectual Property and Ownership</h3>

<p>Attaplace shall at all times retain ownership of the Software as originally downloaded by you and all subsequent downloads of the Software by you. The Software (and the copyright, and other intellectual property rights of whatever nature in the Software, including any modifications made thereto) are and shall remain the property of Attaplace.</p>

<p>Attaplace reserves the right to grant licences to use the Software to third parties.</p>

<h3>Termination</h3>

<p>This EULA agreement is effective from the date you first use the Software and shall continue until terminated. You may terminate it at any time upon written notice to Attaplace.</p>

<p>It will also terminate immediately if you fail to comply with any term of this EULA agreement. Upon such termination, the licenses granted by this EULA agreement will immediately terminate and you agree to stop all access and use of the Software. The provisions that by their nature continue and survive will survive any termination of this EULA agreement. This EULA was created by <a href="https://www.app-privacy-policy.com/app-eula-generator/">App EULA Template Generator from App-Privacy-Policy.com</a> for Attaplace</p>

<h3>Governing Law</h3>

<p>This EULA agreement, and any dispute arising out of or in connection with this EULA agreement, shall be governed by and construed in accordance with the laws of <span class="country">us</span>.</p>
    <html><body>
    '''
    return HttpResponse(html)


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


# class BookmarkViewSet(ReadOnlyModelViewSet):
#     queryset = Bookmark.objects.all()
#     serializer_class = BookmarkSerializer
#     pagination_class = StandardResultsSetPagination
#     permission_classes = [IsAuthenticatedOrReadOnly]
#
#     def get_queryset(self):
#         return Bookmark.objects.filter(writer_user=self.request.user)

    # def destroy(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     self.perform_destroy(instance)
    #     return Response(status=status.HTTP_204_NO_CONTENT)


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
    # callback_url = 'https://anycallbackurlhere'
    client_class = AppleOAuth2Client

    def process_login(self):
        self.user.is_active = True
        self.user.save()
        super().process_login()


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

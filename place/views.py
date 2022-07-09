import json

# from rest_framework_simplejwt.locale import
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from django_filters.rest_framework import DjangoFilterBackend
from djoser.views import UserViewSet
from geopy import Nominatim
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

from achievement.models import Achievement
from location.views import get_location
from notification.models import UserDevice
from notification.notifications import send_impression_notification
from place.models import Place, Group, ClimaticCondition, Category, UserPlaceRelation, GeographicalFeature, \
    TypeTransport, TypeCuisine, CustomUser, Transport, PlaceImage, AccommodationOption, MustSee, FloraFauna, \
    Location, Bookmark, Cuisine, Entertainment, NaturalPhenomena, Safe, UniquenessPlace, Vibe, \
    InterestingFacts, PracticalInformation, WhereToTakeAPicture, UserLocation
from place.serializers.place.create import PlaceCreateSerializer
from place.serializers.place.list import PlaceListSerializer
from place.serializers.place.retrieve import PlaceRetrieveSerializer, PlaceOnAddDeleteBookmarkLikeSerializer
from place.serializers.place_plus import get_plus_place
from place.serializers.serializers import PlaceSerializer, ClimaticConditionSerializer, \
    UserPlaceRelationSerializer, GeographicalFeatureSerializer, \
    TypeTransportSerializer, TypeCuisineSerializer, CustomUserSerializer, \
    LocationSerializer, \
    CustomUserPatchSerializer, CustomUserRetrieveSerializer, UserLocationSerializer
from place.serializers.group_serializer import GroupSerializer
from place.serializers.bookmark_serializer import BookmarkSerializer
from place.serializers.place_nested import TransportSerializer, PlaceImageSerializer, MustSeeSerializer, \
    AccommodationOptionSerializer, CategorySerializer, FloraFaunaSerializer, CuisineSerializer, EntertainmentSerializer, \
    NaturalPhenomenaSerializer, SafeSerializer, UniquenessPlaceSerializer, PracticalInformationSerializer, \
    InterestingFactsSerializer, WhereToTakeAPictureSerializer, VibeSerializer

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


class CuisineViewSet(PlaceNestedViewSet):
    queryset = Cuisine.objects.all()
    serializer_class = CuisineSerializer


class EntertainmentViewSet(PlaceNestedViewSet):
    queryset = Entertainment.objects.all()
    serializer_class = EntertainmentSerializer


class NaturalPhenomenaViewSet(PlaceNestedViewSet):
    queryset = NaturalPhenomena.objects.all()
    serializer_class = NaturalPhenomenaSerializer


class SafeViewSet(PlaceNestedViewSet):
    queryset = Safe.objects.all()
    serializer_class = SafeSerializer


class UniquenessPlaceViewSet(PlaceNestedViewSet):
    queryset = UniquenessPlace.objects.all()
    serializer_class = UniquenessPlaceSerializer


class VibeViewSet(PlaceNestedViewSet):
    queryset = Vibe.objects.all()
    serializer_class = VibeSerializer


class InterestingFactsViewSet(PlaceNestedViewSet):
    queryset = InterestingFacts.objects.all()
    serializer_class = InterestingFactsSerializer


class WhereToTakeAPictureViewSet(PlaceNestedViewSet):
    queryset = WhereToTakeAPicture.objects.all()
    serializer_class = WhereToTakeAPictureSerializer


class PracticalInformationViewSet(PlaceNestedViewSet):
    queryset = PracticalInformation.objects.all()
    serializer_class = PracticalInformationSerializer


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


# class ClimaticConditiommViewSet(PlaceNestedViewSet):
#     queryset = ClimaticConditiomm.objects.all()
#     serializer_class = ClimaticConditiommSerializer


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
            # Send notification
            send_impression_notification(place)
            logger.info('aaaa')

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
    filterset_fields = ['writer_user', 'categories']
    search_fields = ['name', 'locations__country', 'locations__city', ]
    serializer_class = PlaceListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Place.objects.filter(writer_user=self.request.user)


geolocator = Nominatim(user_agent="geoapiExercises")


def city_state_country(coord):
    location = geolocator.reverse(coord, exactly_one=True, language='en')
    address = location.raw['address']
    city = address.get('city', '')
    state = address.get('state', '')
    country = address.get('country', '')
    return city, state, country


class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if serializer.is_valid():
            latitude = serializer.validated_data.get("latitude")
            longitude = serializer.validated_data.get('longitude')
            if latitude and longitude:
                logger.error(city_state_country(f"{latitude}, {longitude}"))
                location = get_location(latitude, longitude)
                if not location:
                    raise ValueError('Can\'t connect to nominatim server')
                logger.info('goood')
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
                    serializer.save(country=country,
                                    city=city,
                                    state=state,
                                    county=county,
                                    latitude=latitude,
                                    longitude=longitude)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return super(LocationViewSet, self).create(request, args, kwargs)


class UserLocationViewSet(ModelViewSet):
    queryset = UserLocation.objects.all()
    serializer_class = UserLocationSerializer
    permission_classes = [IsAuthenticated]


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
        user: CustomUser = CustomUser.objects.filter(email=request.data['email']).first()
        if user:
            try:
                social_account_brands = get_social_account_brands(user)
                if check_has_social_account_error_msg(social_account_brands):
                    return Response(social_account_brands, status=HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS)
                if not user.is_active:
                    user.delete()
            except:
                pass

        return super().create(request, *args, **kwargs)


# class CustomUserPasswordViewSetFromDjoser(UserViewSet):
#     @action(["post"], detail=False)
#     def reset_password(self, request, *args, **kwargs):
#         response: Response = super().reset_password(request, args, kwargs)
#         if 300 > response.status_code >= 200:
#             return Response({'success': True, 'data': None})
#         return Response({'success': False, 'data': None})


# class FollowingViewSet(mixins.ListModelMixin,
#                        viewsets.GenericViewSet):
#     queryset = CustomUser.objects.all()
#     serializer_class = CustomUserPatchSerializer
#
#     def get_queryset(self):
#         return


class CustomUserViewSet(
                        mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        viewsets.GenericViewSet):
    parser_classes = [JSONParser, FormParser, MultiPartParser, ]

    queryset = CustomUser.objects.all()
    default_serializer_class = CustomUserPatchSerializer
    serializer_classes = {
        'list': CustomUserRetrieveSerializer,
        'retrieve': CustomUserRetrieveSerializer,
        # 'create': ,
        # 'put': ,
        'patch': CustomUserPatchSerializer,
    }
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    def get_queryset(self):
        queryset = CustomUser.objects.all()
        # requested_user: CustomUser = self.request.user
        followings = self.request.query_params.get('followings')
        followers = self.request.query_params.get('followers')
        writer_user_id_query_param = self.request.query_params.get('writer_user')
        if writer_user_id_query_param is not None:
            writer_user = CustomUser.objects.filter(pk=writer_user_id_query_param).first()
            if writer_user:
                if followings is not None and followings == 'true':
                    return writer_user.followings.all()
                elif followers is not None and followers == 'true':
                    return queryset.filter(followings=writer_user)
        return queryset

    def update(self, request, *args, **kwargs):
        update_user = CustomUser.objects.filter(pk=kwargs.get('pk')).first()
        if update_user and request.user != update_user:
            return Response({"Error": 'You are not valid user'}, status=status.HTTP_400_BAD_REQUEST)

        return super().update(request, args, kwargs)


    @action(detail=True, methods=['patch'])
    def add_or_delete_following(self, request, pk=None):
        request_user: CustomUser = request.user
        following_user: CustomUser = CustomUser.objects.filter(pk=pk).first()

        if following_user:
            if request_user.followings.filter(pk=pk).exists():
                request_user.followings.remove(following_user)
                user_followers_amount = CustomUser.objects.filter(followings=following_user).count()
                is_following = False
            else:
                request_user.followings.add(following_user)
                is_following = True
                user_followers_amount = CustomUser.objects.filter(followings=following_user).count()
            return Response(
                {
                    'is_following': is_following,
                    'user_followers_amount': user_followers_amount,
                }
            )

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

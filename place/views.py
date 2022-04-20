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

from place.models import Place, Group, ClimaticConditions, Category, UserPlaceRelation, GeographicalFeature, \
    TypeTransport, TypeCuisine, CustomUser, Bookmark
from place.serializers.place.list import PlaceListSerializer
from place.serializers.place.retrieve import PlaceRetrieveSerializer
from place.serializers.serializers import PlaceSerializer, GroupSerializer, ClimateSerializer, \
    CategorySerializer, UserPlaceRelationSerializer, GeographicalFeatureSerializer, \
    TypeTransportSerializer, TypeCuisineSerializer, CustomUserSerializer, BookmarkSerializer, \
    CustomSocialLoginSerializer

from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
# from rest_auth.registration.views import SocialLoginView


from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer

# class CustomRenderer(JSONRenderer):
#
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
#
# geolocator = Nominatim(user_agent="location")


plus_place = [
    # TODO: required field for every object
    {
        "header": "General Info",
        "key": None,
        "children": [
            {
                "placeholder": "Name",
                'title': 'Name',
                'required': True,
                "key": 'name',
                'field_type': 'charfield'
            },

            {
                "placeholder": "Nickname",
                'title': 'Nickname',
                "key": 'nickname',
                'field_type': 'charfield'
            },

            {
                "placeholder": "Overview",
                'title': "Overview",
                'required': True,
                "key": 'description',
                'field_type': "textfield"
            },

            {
                "placeholder": "Rating",
                'title': "Rating",
                'required': True,
                "key": 'rating',
                'field_type': "intfield",
            }

        ]
    },

    {
        "header": "Images",
        "key": 'images',
        "children": [

            {
                'title': "Images",
                'required': True,
                "key": 'path',
                'field_type': "imagefield",
            },

        ]
    },

    {
        "header": "Category",
        "key": 'category',

        "children": [
            {
                'title': 'Category',
                "key": 'category',
                'required': True,
                'field_type': 'multiselect',
                "options": [
                    {"text": 'Active', "value": 1, },
                    {"text": 'Adventures', "value": 1, },
                    {"text": 'Alien', "value": 1, },
                    {"text": 'Animal', "value": 1, },
                    {"text": 'Cinema', "value": 1, },
                    {"text": 'Cultural', "value": 1, },
                    {"text": 'Digging', "value": 1, },
                    {"text": 'Eco', "value": 1, },
                    {"text": 'Event', "value": 1, },
                    {"text": 'Exotic', "value": 1, },
                    {"text": 'Extreme', "value": 1, },
                    {"text": 'Family', "value": 1, },
                    {"text": 'From 7 d', "value": 1, },
                    {"text": 'Gastro', "value": 1, },
                    {"text": 'Gothic', "value": 1, },
                    {"text": 'Jailoo', "value": 1, },
                    {"text": 'Mystery', "value": 1, },
                    {"text": 'Philosophy', "value": 1, },
                    {"text": 'Recreation', "value": 1, },
                    {"text": 'Pilgrimage', "value": 1, },
                    {"text": 'Spirit', "value": 1, },
                    {"text": 'Up to 3', "value": 1, },
                    {"text": 'Up to 7 d', "value": 1, },
                    {"text": 'Honeymoon', "value": 1, },
                    {"text": 'Urban', "value": 1, },
                    {"text": 'Welness', "value": 1, },
                ]
            },

        ]
    },

    {
        "header": "Civilization",
        "key": None,

        "children": [
            {
                "placeholder": "Population",
                'title': "Population",
                'key': "population",
                'field_type': "intfield"
            },

            {
                "placeholder": "Type Of People Around",
                'title': "Type Of People Around",
                'key': "type_of_people_around",
                'field_type': "textfield"
            },

            {
                "placeholder": "Turist Rating",
                'title': "Turist Rating",
                'key': "turist_rating",
                'field_type': "intfield"
            },

            {
                "placeholder": "Nation",
                'title': "Nation",
                'key': "nation",
                'field_type': "charfield"
            },

            {
                "placeholder": "Language",
                'title': "Language",
                'key': "language",
                'field_type': "charfield"
            },

            {
                "placeholder": "Culture",
                'title': 'Culture',
                'key': 'culture',
                'field_type': 'textfield'
            },

            {
                "placeholder": "Currency",
                'title': "Currency",
                'key': "currency",
                'field_type': "charfield"
            },

            {
                "placeholder": "Currency Buying Advice",
                'title': 'Currency Buying Advice',
                'key': 'currency_buying_advice',
                'field_type': 'textfield'
            },

            {
                "placeholder": "Sim Cards",
                'title': "Sim Cards",
                'key': "simcards",
                'field_type': "charfield"
            },

            {
                "placeholder": "Internet",
                'title': "Internet",
                'key': "internet",
                'field_type': "charfield"
            },

            {
                "placeholder": "Payment Method",
                'title': 'Pay Online Or By Card',
                'key': 'pay_online_or_by_card',
                'field_type': 'textfield'
            },

        ]
    },
    {
        "header": "Climate",
        "key": None,
        "children": [
            {
                "placeholder": "Climate",
                'title': 'Climate',
                'key': 'climate',
                'required': True,
                'field_type': 'picker',
                "options": [
                    {"text": 'Tropical', "value": 1, },
                    {"text": 'Dry', "value": 1, },
                    {"text": 'Mild', "value": 1, },
                    {"text": 'Continental', "value": 1, },
                    {"text": 'Polar', "value": 1, },
                ],
            },

            {
                "placeholder": "Climate Description",
                'title': 'Climate Description',
                'key': 'climate_description',
                'field_type': 'charfield'
            },

        ]
    },

    {
        "header": "Geographical Feature",
        'key': None,
        "children": [
            {
                "placeholder": "Geographical Feature",
                'title': 'Geographical Feature',
                'key': 'geographical_feature',
                'field_type': 'charfield'
            },

            {
                "placeholder": "Geographical Feature Description",
                'title': 'Geographical Feature Description',
                'key': 'geographical_feature_description',
                'field_type': 'charfield'
            },

        ]
    },

    {
        "header": "Transport",
        "key": "transport",
        "nested": [
            {
                "placeholder": "Kind Of Transport",
                'title': 'Kind Of Transport',
                "key": "type_transport",
                'field_type': 'picker',
                "options": [
                    {"text": 'Walking', "value": 1, },
                    {"text": 'Biking', "value": 2, },
                    {"text": 'Cars', "value": 3, },
                    {"text": 'Trains', "value": 4, },
                    {"text": 'Buses', "value": 5, },
                    {"text": 'Boats', "value": 6, },
                    {"text": 'Subways', "value": 7, },
                    {"text": 'BusesAerial Tramways', "value": 8, },
                    {"text": 'Flying', "value": 9, },
                    {"text": 'Funiculars', "value": 10, },
                ],
            },

            {
                "placeholder": "Transport Price",
                'title': "Transport Price",
                'key': "price",
                'field_type': 'floatfield',
            },

            {
                "placeholder": "Transport Description",
                'title': "Transport Description",
                'key': "description",
                'field_type': "textfield",
            },

            {
                "placeholder": "Transport Comfortable",
                'title': "Transport Comfortable",
                'key': "comfortable",
                'field_type': "picker",
                "options": [
                    {"text": 'Very Comfortable', "value": 1, },
                    {"text": 'Comfortable', "value": 1, },
                    {"text": 'Average', "value": 1, },
                    {"text": 'Durable', "value": 1, },
                    {"text": 'Totally Uncomfortable', "value": 1, },
                ],
            },

            {
                'title': "Transport Image",
                'key': 'image',
                'field_type': "imagefield",
            }

        ]
    },

    {
        # TODO: header nuzhno pridumat cto by oharektezowala children
        "header": "---------------------------------------------------------------------------------------------------------------------------------------------------------------------",
        "key": None,
        "nested": [
            {
                "placeholder": "Nearest Airport",
                'title': 'Nearest Airport',
                "key": "nearest_airport",
                'field_type': 'charfield',

            },

            {
                "placeholder": "How To Get There",
                'title': "How To Get There",
                'key': "how_to_get_there",
                'required': True,
                'field_type': "textfield",
            },

        ]
    },

    {
        "header": "Cuisine",
        "key": "cuisine",
        "nested": [
            {
                "placeholder": "Kind Of Cuisine",
                'title': 'Kind Of Cuisine',
                "key": "name",
                'field_type': 'picker',
                "options": [
                    {"text": 'French Cuisine', "value": 1, },
                    {"text": 'Chinese Cuisine', "value": 1, },
                    {"text": 'Japanese Cuisine', "value": 1, },
                    {"text": 'Indian Cuisine', "value": 1, },
                    {"text": 'Italian Cuisine', "value": 1, },
                    {"text": 'Greek Cuisine', "value": 1, },
                    {"text": 'Spanish Cuisine', "value": 1, },
                    {"text": 'Mediterranean Cuisine', "value": 1, },
                ],
            },

            {
                "placeholder": "Cuisine Price",
                'title': "Cuisine Price",
                'key': "price",
                'field_type': "floatfield",
            },

            {
                "placeholder": "Transport Description",
                'title': "Transport Description",
                'key': "description",
                'field_type': "textfield",
            },

            {
                'title': "Cuisine Image",
                'key': 'image',
                'field_type': "imagefield",
            }

        ]
    },

    {
        "header": "Safe",
        "key": "safe",
        "nested": [
            {
                "placeholder": "Safe Name",
                'title': 'Safe Name',
                "key": "name",
                'field_type': 'charfield',
            },

            {
                "placeholder": "How Dangerous",
                'title': "How Dangerous",
                'key': "how_dangerous",
                'field_type': "picker",
                "options": [
                    {"text": 'Very Safe', "value": 1, },
                    {"text": 'Safe', "value": 1, },
                    {"text": 'Average', "value": 1, },
                    {"text": 'Somewhat Dangerous', "value": 1, },
                    {"text": 'Dangerous', "value": 1, },
                ],
            },

            {
                "placeholder": "Rating Danger",
                'title': "Rating Danger",
                'key': "rating_danger",
                'field_type': "intfield",
            },

            {
                "placeholder": "Description",
                'title': "Description",
                'key': 'description',
                'field_type': "textfield",
            }

        ]
    },

    {
        "header": "Entertainment",
        "key": "entertainment",
        "nested": [
            {
                "placeholder": "Entertainment Name",
                'title': 'Entertainment Name',
                "key": "name",
                'field_type': 'charfield',
            },

            {
                "placeholder": "Description",
                'title': "Description",
                'key': 'description',
                'field_type': "textfield",
            },

            {
                'title': "Cuisine Image",
                'key': 'image',
                'field_type': "imagefield",
            }

        ]
    },

    {
        "header": "Natural Phenomena",
        "key": "natural_phenomena",
        "nested": [
            {
                "placeholder": "Natural Phenomena Name",
                'title': 'Natural Phenomena Name',
                "key": "name",
                'field_type': 'charfield',
            },

            {
                "placeholder": "Description",
                'title': "Description",
                'key': 'description',
                'field_type': "textfield",
            },

            {
                'title': "Cuisine Image",
                'key': 'image',
                'field_type': "imagefield",
            }

        ]
    },

    {
        "header": "Accommodation Options",
        "key": "accommodation_Option",
        "nested": [
            {
                "placeholder": "Accommodation Options Name",
                'title': 'Accommodation Options Name',
                "key": "name",
                'field_type': 'charfield',
            },

            {
                "placeholder": "Price",
                'title': "Price",
                'key': "price",
                'field_type': "floatfield",
            },

            {
                "placeholder": "Description",
                'title': "Description",
                'key': 'description',
                'field_type': "textfield",
            },

        ]
    },

    {
        "header": "Uniqueness Place",
        "key": "uniqueness_place",
        "nested": [
            {
                "placeholder": "Uniqueness Place Name",
                'title': 'Uniqueness Place Name',
                "key": "name",
                'required': True,
                'field_type': 'charfield',
            },

            {
                "placeholder": "Description",
                'title': "Description",
                'key': 'description',
                'required': True,
                'field_type': "textfield",
            },

            {
                'title': "Uniqueness Place Image",
                'key': 'image',
                'field_type': "imagefield",
            }

        ]
    },

    {
        "header": "Must See",
        "key": "must_see",
        "nested": [
            {
                "placeholder": "Must See Name",
                'title': 'Must See Name',
                "key": "name",
                'required': True,
                'field_type': 'charfield',
            },

            {
                "placeholder": "Description",
                'title': "Description",
                'key': 'description',
                'required': True,
                'field_type': "textfield",
            },

            {
                'title': "Must See Image",
                'key': 'image',
                'field_type': "imagefield",
            }

        ]
    },

    {
        "header": "Vibe",
        "key": "vibe",
        "nested": [
            {
                "placeholder": "Vibe Name",
                'title': 'Vibe Name',
                "key": "name",
                'field_type': 'charfield',
            },
            {
                'title': "Vibe Image",
                'key': 'image',
                'field_type': "imagefield",
            }

        ]
    },

    {
        "header": "Where To Take A Picture",
        "key": "where_to_take_a_picture",
        "nested": [
            {
                "placeholder": "Where To Take A Picture Name",
                'title': 'Where To Take A Picture Name',
                "key": "name",
                'field_type': 'charfield',
            },

            {
                "placeholder": "Description",
                'title': "Description",
                'key': 'description',
                'field_type': "textfield",
            },

            {
                'title': "Where To Take A Picture Image",
                'key': 'image',
                'field_type': "imagefield",
            }

        ]
    },

    {
        "header": "Interesting Facts",
        "key": "interesting_fact",
        "nested": [
            {
                "placeholder": "Description",
                'title': "Description",
                'key': 'description',
                'field_type': "textfield",
            },

            {
                'title': "Interesting Facts Image",
                'key': 'image',
                'field_type': "imagefield",
            }

        ]
    },

    {
        "header": "Practical Information",
        "key": "practical_information",
        "nested": [
            {
                "placeholder": "Description",
                'title': "Description",
                'key': 'description',
                'field_type': "textfield",
            },
        ]
    },
    {
        "header": "FloraAndFauna",
        "key": "flora_fauna",
        "nested": [
            {
                "placeholder": "FloraAndFauna Name",
                'title': 'FloraAndFauna Name',
                "key": "name",
                'field_type': 'charfield',
            },
            {
                "placeholder": "Description",
                'title': "Description",
                'key': 'description',
                'field_type': "textfield",
            },
            {
                'title': "FloraAndFauna Image",
                'key': 'image',
                'field_type': "imagefield",
            }
        ]
    },
]


class PlaceViewSet(ModelViewSet):
    queryset = Place.objects.all()
    default_serializer_class = PlaceSerializer
    serializer_classes = {
        'list': PlaceListSerializer,
        'retrieve': PlaceRetrieveSerializer,
        # 'create': default_serializer_class,
        # 'put': default_serializer_class,
        # 'patch': default_serializer_class,
    }

    def retrieve(self, request, *args, **kwargs):
        queryset = Place.objects.filter(name=self.get_object().name)
        # print(queryset)
        serializer = PlaceSerializer(queryset, many=True, context={"request": request})

        # cto by serializer.data wytashit iz lista
        no_list_serializer = serializer.data[0]

        section = []
        owerview_section = {}

        reapet_field = ''

        new_serializer = no_list_serializer.copy()

        for field in no_list_serializer:

            if field in ['name', 'description']:
                owerview_section[field] = new_serializer[field]
                del new_serializer[field]

        new_serializer['owerview'] = owerview_section

        no_list_serializer = new_serializer.copy()


        for field in no_list_serializer:
            # if field in ['name', 'description']:
            #     owerview_section[field] = new_serializer[field]
            #     del new_serializer[field]


            if type(no_list_serializer[field]) is list and no_list_serializer[field] != [] and field not in ['category',
                                                                                                             'images']:
                print(field)
                for len_list in range(len(no_list_serializer[field])):


                    if 'name' in no_list_serializer[field][len_list] and no_list_serializer[field][len_list]['name'] != '':
                        name = f'{no_list_serializer[field][len_list]["name"]}'
                        del no_list_serializer[field][len_list]["name"]
                    else:
                        name = ''

                    if 'image' in no_list_serializer[field][len_list] and no_list_serializer[field][len_list]['image'] != '':
                        image = f'<img src={no_list_serializer[field][len_list]["image"]}/>'
                        del no_list_serializer[field][len_list]["image"]
                    else:
                        image = ''

                    if 'price' in no_list_serializer[field][len_list] and no_list_serializer[field][len_list]['price'] != '':
                        price = f'<p>Price: {no_list_serializer[field][len_list]["price"]}</p>'
                        del no_list_serializer[field][len_list]["price"]
                    else:
                        price = ''

                    if 'comfortable' in no_list_serializer[field][len_list] and no_list_serializer[field][len_list]['comfortable'] != '':
                        comfortable = f'<p>Comfortable: {no_list_serializer[field][len_list]["comfortable"]}</p>'
                        del no_list_serializer[field][len_list]["comfortable"]
                    else:
                        comfortable = ''

                    if 'how_dangerous' in no_list_serializer[field][len_list] and no_list_serializer[field][len_list][
                        'how_dangerous'] != '':
                        how_dangerous = f'<p>How Dangerous: {no_list_serializer[field][len_list]["how_dangerous"]}</p>'
                        del no_list_serializer[field][len_list]["how_dangerous"]
                    else:
                        how_dangerous = ''

                    if 'rating_danger' in no_list_serializer[field][len_list] and no_list_serializer[field][len_list][
                        'rating_danger'] != '':
                        rating_danger = f'<p>Rating Danger: {no_list_serializer[field][len_list]["rating_danger"]}</p>'
                        del no_list_serializer[field][len_list]["rating_danger"]
                    else:
                        rating_danger = ''

                    if 'continent' in no_list_serializer[field][len_list] and no_list_serializer[field][len_list][
                        'continent'] != '':
                        continent = f'<p>Continent: {no_list_serializer[field][len_list]["continent"]}</p>'
                        del no_list_serializer[field][len_list]["continent"]
                    else:
                        continent = ''

                    if 'country' in no_list_serializer[field][len_list] and no_list_serializer[field][len_list][
                        'country'] != '':
                        country = f'<p>Country: {no_list_serializer[field][len_list]["country"]}</p>'
                        del no_list_serializer[field][len_list]["country"]
                    else:
                        country = ''

                    if 'region' in no_list_serializer[field][len_list] and no_list_serializer[field][len_list][
                        'region'] != '':
                        region = f'<p>region: {no_list_serializer[field][len_list]["region"]}</p>'
                        del no_list_serializer[field][len_list]["region"]
                    else:
                        region = ''

                    if 'city' in no_list_serializer[field][len_list] and no_list_serializer[field][len_list][
                        'city'] != '':
                        city = f'<p>City: {no_list_serializer[field][len_list]["city"]}</p>'
                        del no_list_serializer[field][len_list]["city"]
                    else:
                        city = ''

                    if 'latitude' in no_list_serializer[field][len_list] and no_list_serializer[field][len_list][
                        'latitude'] != '':
                        latitude = f'<p>Latitude: {no_list_serializer[field][len_list]["latitude"]}</p>'
                        del no_list_serializer[field][len_list]["latitude"]
                    else:
                        latitude = ''

                    if 'longitude' in no_list_serializer[field][len_list] and no_list_serializer[field][len_list][
                        'longitude'] != '':
                        longitude = f'<p>Longitude: {no_list_serializer[field][len_list]["longitude"]}</p>'
                        del no_list_serializer[field][len_list]["longitude"]
                    else:
                        longitude = ''

                    if 'nearest_place' in no_list_serializer[field][len_list] and no_list_serializer[field][len_list][
                        'nearest_place'] != '':
                        nearest_place = f'<p>nearest_place: {no_list_serializer[field][len_list]["nearest_place"]}</p>'
                        del no_list_serializer[field][len_list]["nearest_place"]
                    else:
                        nearest_place = ''


                    if field in ['flora_fauna']:
                        new_serializer[field][len_list]['display_type'] = 'grid'
                        if reapet_field != field:
                            # print('type: ', len(no_list_serializer[field]))
                            if 'description' not in no_list_serializer[field][len_list]:
                                new_serializer[field][len_list]['children'] = [
                                    {"id": no_list_serializer[field][len_list]['id'],
                                     "title": f"{name}",
                                     "image": f"{image}",
                                     "description": f"{image}{price}{comfortable}{how_dangerous}{rating_danger}{continent}{country}{region}{city}{latitude}{longitude}{nearest_place}"}]
                            else:
                                new_serializer[field][len_list]['children'] = [
                                    {"id": no_list_serializer[field][len_list]['id'],
                                     "title": f"{name}",
                                     "image": f"{image}",
                                     "description": f"{image}{price}{comfortable}{how_dangerous}{rating_danger}{continent}{country}{region}{city}{latitude}{longitude}{nearest_place}<p>{no_list_serializer[field][len_list]['description']}</p>"}]
                                del no_list_serializer[field][len_list]['description']
                            del no_list_serializer[field][len_list]['id']

                            no_list_serializer[field][len_list]['title'] = field.capitalize().replace("_", " ")
                            no_list_serializer[field][len_list]['key'] = field.lower().replace(" ", "")
                            no_list_serializer[field][len_list]['icon_name'] = "article".lower().replace(" ", "")

                            reapet_field = field
                            section.append(no_list_serializer[field][len_list])

                        else:

                            if 'description' not in no_list_serializer[field][len_list]:
                                new_serializer[field][0]['children'].append(
                                    {"id": no_list_serializer[field][len_list]['id'],
                                     "title": f"{name}",
                                     "image": f"{image}",
                                     "description": f"{image}{price}{comfortable}{how_dangerous}{rating_danger}{continent}{country}{region}{city}{latitude}{longitude}{nearest_place}"})
                            else:
                                new_serializer[field][0]['children'].append(
                                    {"id": no_list_serializer[field][len_list]['id'],
                                     "title": f"{name}",
                                     "image": f"{image}",
                                     "description": f"{image}{price}{comfortable}{how_dangerous}{rating_danger}{continent}{country}{region}{city}{latitude}{longitude}{nearest_place}<p>{no_list_serializer[field][len_list]['description']}</p>"})
                    else:
                        if reapet_field != field:
                            # print('type: ', len(no_list_serializer[field]))

                            new_serializer[field][len_list]['display_type'] = 'drop_down'

                            if field in ['location', 'practical_information', 'interesting_fact']:
                                new_serializer[field][len_list]['display_type'] = 'simple'

                            if 'description' not in no_list_serializer[field][len_list]:
                                new_serializer[field][len_list]['children'] = [
                                    {"id": no_list_serializer[field][len_list]['id'],
                                     "title": f"{name}",
                                     "description": f"{image}{price}{comfortable}{how_dangerous}{rating_danger}{continent}{country}{region}{city}{latitude}{longitude}{nearest_place}"}]
                            else:
                                new_serializer[field][len_list]['children'] = [
                                    {"id": no_list_serializer[field][len_list]['id'],
                                     "title": f"{name}",
                                     "description": f"{image}{price}{comfortable}{how_dangerous}{rating_danger}{continent}{country}{region}{city}{latitude}{longitude}{nearest_place}<p>{no_list_serializer[field][len_list]['description']}</p>"}]
                                del no_list_serializer[field][len_list]['description']
                            del no_list_serializer[field][len_list]['id']

                            no_list_serializer[field][len_list]['title'] = field.capitalize().replace("_", " ")
                            no_list_serializer[field][len_list]['key'] = field.lower().replace(" ", "")
                            no_list_serializer[field][len_list]['icon_name'] = "article".lower().replace(" ", "")

                            reapet_field = field
                            section.append(no_list_serializer[field][len_list])

                        else:

                            if 'description' not in no_list_serializer[field][len_list]:
                                new_serializer[field][0]['children'].append(
                                    {"id": no_list_serializer[field][len_list]['id'],
                                     "title": f"{name}",
                                     "description": f"{image}{price}{comfortable}{how_dangerous}{rating_danger}{continent}{country}{region}{city}{latitude}{longitude}{nearest_place}"})
                            else:
                                new_serializer[field][0]['children'].append(
                                    {"id": no_list_serializer[field][len_list]['id'],
                                     "title": f"{name}",
                                     "description": f"{image}{price}{comfortable}{how_dangerous}{rating_danger}{continent}{country}{region}{city}{latitude}{longitude}{nearest_place}<p>{no_list_serializer[field][len_list]['description']}</p>"})

                del new_serializer[field]
        # new_serializer['owerview'] = owerview_section

        new_serializer['sections'] = section


        return Response(new_serializer)

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    @action(detail=False, methods=["get"])
    def plus_place(self, request):
        return Response(plus_place)

    @action(detail=False, methods=["get"])
    def test(self, request):
        queryset = Place.objects.all()
        serializer = PlaceSerializer(queryset, many=True)
        return Response(serializer.data)

#
# class PlaceViewSet(ModelViewSet, ListView):
#     queryset = Place.objects.all()
#     serializer_class = PlaceSerializer
#     # renderer_classes = [CustomRenderer, BrowsableAPIRenderer]
#     filter_backends = [DjangoFilterBackend, SearchFilter]
#     filterset_fields = ['category', 'home_page']
#     search_fields = ['name', 'nickname']
#     permission_classes = [IsAuthenticatedOrReadOnly]
#
#     # mapping serializer into the action
#     # pagination_class = PlaceAPIListPagination
#
#
#     def list(self, request, *args, **kwargs):
#         queryset = Place.objects.all()
#         serializer = PlaceSerializer(queryset, many=True, context={"request": request})
#         new_serializer_list = []
#         for index_data in range(len(serializer.data)):
#             new_serializer = serializer.data[index_data].copy()
#             for field in serializer.data[index_data]:
#
#                 if field not in ['id', 'name', 'description', 'images', 'rating', 'location', 'writer_user']:
#                     del new_serializer[field]
#
#                 if field == 'writer_user':
#                     del new_serializer[field]['id']
#                     del new_serializer[field]['is_active']
#
#             new_serializer_list.append(new_serializer)
#
#         return Response(new_serializer_list)
#
    # def retrieve(self, request, *args, **kwargs):
    #     queryset = Place.objects.filter(name=self.get_object().name)
    #     # print(queryset)
    #     serializer = PlaceSerializer(queryset, many=True, context={"request": request})
    #
    #     # cto by serializer.data wytashit iz lista
    #     no_list_serializer = serializer.data[0]
    #
    #     section = []
    #     owerview_section = {}
    #
    #     reapet_field = ''
    #
    #     new_serializer = no_list_serializer.copy()
    #
    #     for field in no_list_serializer:
    #
    #         if field in ['name', 'description']:
    #             owerview_section[field] = new_serializer[field]
    #             del new_serializer[field]
    #
    #     new_serializer['owerview'] = owerview_section
    #
    #     no_list_serializer = new_serializer.copy()
    #
    #
    #     for field in no_list_serializer:
    #         # if field in ['name', 'description']:
    #         #     owerview_section[field] = new_serializer[field]
    #         #     del new_serializer[field]
    #
    #
    #         if type(no_list_serializer[field]) is list and no_list_serializer[field] != [] and field not in ['category',
    #                                                                                                          'images']:
    #             print(field)
    #             for len_list in range(len(no_list_serializer[field])):
    #
    #
    #                 if 'name' in no_list_serializer[field][len_list] and no_list_serializer[field][len_list]['name'] != '':
    #                     name = f'{no_list_serializer[field][len_list]["name"]}'
    #                     del no_list_serializer[field][len_list]["name"]
    #                 else:
    #                     name = ''
    #
    #                 if 'image' in no_list_serializer[field][len_list] and no_list_serializer[field][len_list]['image'] != '':
    #                     image = f'<img src={no_list_serializer[field][len_list]["image"]}/>'
    #                     del no_list_serializer[field][len_list]["image"]
    #                 else:
    #                     image = ''
    #
    #                 if 'price' in no_list_serializer[field][len_list] and no_list_serializer[field][len_list]['price'] != '':
    #                     price = f'<p>Price: {no_list_serializer[field][len_list]["price"]}</p>'
    #                     del no_list_serializer[field][len_list]["price"]
    #                 else:
    #                     price = ''
    #
    #                 if 'comfortable' in no_list_serializer[field][len_list] and no_list_serializer[field][len_list]['comfortable'] != '':
    #                     comfortable = f'<p>Comfortable: {no_list_serializer[field][len_list]["comfortable"]}</p>'
    #                     del no_list_serializer[field][len_list]["comfortable"]
    #                 else:
    #                     comfortable = ''
    #
    #                 if 'how_dangerous' in no_list_serializer[field][len_list] and no_list_serializer[field][len_list][
    #                     'how_dangerous'] != '':
    #                     how_dangerous = f'<p>How Dangerous: {no_list_serializer[field][len_list]["how_dangerous"]}</p>'
    #                     del no_list_serializer[field][len_list]["how_dangerous"]
    #                 else:
    #                     how_dangerous = ''
    #
    #                 if 'rating_danger' in no_list_serializer[field][len_list] and no_list_serializer[field][len_list][
    #                     'rating_danger'] != '':
    #                     rating_danger = f'<p>Rating Danger: {no_list_serializer[field][len_list]["rating_danger"]}</p>'
    #                     del no_list_serializer[field][len_list]["rating_danger"]
    #                 else:
    #                     rating_danger = ''
    #
    #                 if 'continent' in no_list_serializer[field][len_list] and no_list_serializer[field][len_list][
    #                     'continent'] != '':
    #                     continent = f'<p>Continent: {no_list_serializer[field][len_list]["continent"]}</p>'
    #                     del no_list_serializer[field][len_list]["continent"]
    #                 else:
    #                     continent = ''
    #
    #                 if 'country' in no_list_serializer[field][len_list] and no_list_serializer[field][len_list][
    #                     'country'] != '':
    #                     country = f'<p>Country: {no_list_serializer[field][len_list]["country"]}</p>'
    #                     del no_list_serializer[field][len_list]["country"]
    #                 else:
    #                     country = ''
    #
    #                 if 'region' in no_list_serializer[field][len_list] and no_list_serializer[field][len_list][
    #                     'region'] != '':
    #                     region = f'<p>region: {no_list_serializer[field][len_list]["region"]}</p>'
    #                     del no_list_serializer[field][len_list]["region"]
    #                 else:
    #                     region = ''
    #
    #                 if 'city' in no_list_serializer[field][len_list] and no_list_serializer[field][len_list][
    #                     'city'] != '':
    #                     city = f'<p>City: {no_list_serializer[field][len_list]["city"]}</p>'
    #                     del no_list_serializer[field][len_list]["city"]
    #                 else:
    #                     city = ''
    #
    #                 if 'latitude' in no_list_serializer[field][len_list] and no_list_serializer[field][len_list][
    #                     'latitude'] != '':
    #                     latitude = f'<p>Latitude: {no_list_serializer[field][len_list]["latitude"]}</p>'
    #                     del no_list_serializer[field][len_list]["latitude"]
    #                 else:
    #                     latitude = ''
    #
    #                 if 'longitude' in no_list_serializer[field][len_list] and no_list_serializer[field][len_list][
    #                     'longitude'] != '':
    #                     longitude = f'<p>Longitude: {no_list_serializer[field][len_list]["longitude"]}</p>'
    #                     del no_list_serializer[field][len_list]["longitude"]
    #                 else:
    #                     longitude = ''
    #
    #                 if 'nearest_place' in no_list_serializer[field][len_list] and no_list_serializer[field][len_list][
    #                     'nearest_place'] != '':
    #                     nearest_place = f'<p>nearest_place: {no_list_serializer[field][len_list]["nearest_place"]}</p>'
    #                     del no_list_serializer[field][len_list]["nearest_place"]
    #                 else:
    #                     nearest_place = ''
    #
    #
    #                 if field in ['flora_fauna']:
    #                     new_serializer[field][len_list]['display_type'] = 'grid'
    #                     if reapet_field != field:
    #                         # print('type: ', len(no_list_serializer[field]))
    #                         if 'description' not in no_list_serializer[field][len_list]:
    #                             new_serializer[field][len_list]['children'] = [
    #                                 {"id": no_list_serializer[field][len_list]['id'],
    #                                  "title": f"{name}",
    #                                  "image": f"{image}",
    #                                  "description": f"{image}{price}{comfortable}{how_dangerous}{rating_danger}{continent}{country}{region}{city}{latitude}{longitude}{nearest_place}"}]
    #                         else:
    #                             new_serializer[field][len_list]['children'] = [
    #                                 {"id": no_list_serializer[field][len_list]['id'],
    #                                  "title": f"{name}",
    #                                  "image": f"{image}",
    #                                  "description": f"{image}{price}{comfortable}{how_dangerous}{rating_danger}{continent}{country}{region}{city}{latitude}{longitude}{nearest_place}<p>{no_list_serializer[field][len_list]['description']}</p>"}]
    #                             del no_list_serializer[field][len_list]['description']
    #                         del no_list_serializer[field][len_list]['id']
    #
    #                         no_list_serializer[field][len_list]['title'] = field.capitalize().replace("_", " ")
    #                         no_list_serializer[field][len_list]['key'] = field.lower().replace(" ", "")
    #                         no_list_serializer[field][len_list]['icon_name'] = "article".lower().replace(" ", "")
    #
    #                         reapet_field = field
    #                         section.append(no_list_serializer[field][len_list])
    #
    #                     else:
    #
    #                         if 'description' not in no_list_serializer[field][len_list]:
    #                             new_serializer[field][0]['children'].append(
    #                                 {"id": no_list_serializer[field][len_list]['id'],
    #                                  "title": f"{name}",
    #                                  "image": f"{image}",
    #                                  "description": f"{image}{price}{comfortable}{how_dangerous}{rating_danger}{continent}{country}{region}{city}{latitude}{longitude}{nearest_place}"})
    #                         else:
    #                             new_serializer[field][0]['children'].append(
    #                                 {"id": no_list_serializer[field][len_list]['id'],
    #                                  "title": f"{name}",
    #                                  "image": f"{image}",
    #                                  "description": f"{image}{price}{comfortable}{how_dangerous}{rating_danger}{continent}{country}{region}{city}{latitude}{longitude}{nearest_place}<p>{no_list_serializer[field][len_list]['description']}</p>"})
    #                 else:
    #                     if reapet_field != field:
    #                         # print('type: ', len(no_list_serializer[field]))
    #
    #                         new_serializer[field][len_list]['display_type'] = 'drop_down'
    #
    #                         if field in ['location', 'practical_information', 'interesting_fact']:
    #                             new_serializer[field][len_list]['display_type'] = 'simple'
    #
    #                         if 'description' not in no_list_serializer[field][len_list]:
    #                             new_serializer[field][len_list]['children'] = [
    #                                 {"id": no_list_serializer[field][len_list]['id'],
    #                                  "title": f"{name}",
    #                                  "description": f"{image}{price}{comfortable}{how_dangerous}{rating_danger}{continent}{country}{region}{city}{latitude}{longitude}{nearest_place}"}]
    #                         else:
    #                             new_serializer[field][len_list]['children'] = [
    #                                 {"id": no_list_serializer[field][len_list]['id'],
    #                                  "title": f"{name}",
    #                                  "description": f"{image}{price}{comfortable}{how_dangerous}{rating_danger}{continent}{country}{region}{city}{latitude}{longitude}{nearest_place}<p>{no_list_serializer[field][len_list]['description']}</p>"}]
    #                             del no_list_serializer[field][len_list]['description']
    #                         del no_list_serializer[field][len_list]['id']
    #
    #                         no_list_serializer[field][len_list]['title'] = field.capitalize().replace("_", " ")
    #                         no_list_serializer[field][len_list]['key'] = field.lower().replace(" ", "")
    #                         no_list_serializer[field][len_list]['icon_name'] = "article".lower().replace(" ", "")
    #
    #                         reapet_field = field
    #                         section.append(no_list_serializer[field][len_list])
    #
    #                     else:
    #
    #                         if 'description' not in no_list_serializer[field][len_list]:
    #                             new_serializer[field][0]['children'].append(
    #                                 {"id": no_list_serializer[field][len_list]['id'],
    #                                  "title": f"{name}",
    #                                  "description": f"{image}{price}{comfortable}{how_dangerous}{rating_danger}{continent}{country}{region}{city}{latitude}{longitude}{nearest_place}"})
    #                         else:
    #                             new_serializer[field][0]['children'].append(
    #                                 {"id": no_list_serializer[field][len_list]['id'],
    #                                  "title": f"{name}",
    #                                  "description": f"{image}{price}{comfortable}{how_dangerous}{rating_danger}{continent}{country}{region}{city}{latitude}{longitude}{nearest_place}<p>{no_list_serializer[field][len_list]['description']}</p>"})
    #
    #             del new_serializer[field]
    #     # new_serializer['owerview'] = owerview_section
    #
    #     new_serializer['sections'] = section
    #
    #
    #     return Response(new_serializer)
    #
    # @action(detail=False, methods=["get"])
    # def plus_place(self, request):
    #     # queryset = Place.objects.all()
    #     # serializer = PlaceSerializer(queryset, many=True)
    #     # return Response(serializer.data)
    #     return Response(plus_place)
    #
    # def perform_create(self, serializer):
    #     address = serializer.initial_data["name"]
    #     g = geolocator.geocode(address)
    #     lat = g.latitude
    #     lng = g.longitude
    #     pnt = Point(lng, lat)
    #     print('pnt_create: ', pnt)
    #     serializer.save(location=pnt)
    #
    # def perform_update(self, serializer):
    #     address = serializer.initial_data["address"]
    #     g = geolocator.geocode(address)
    #     lat = g.latitude
    #     lng = g.longitude
    #     pnt = Point(lng, lat)
    #     print('pnt_update: ', pnt)
    #     serializer.save(location=pnt)


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
    queryset = ClimaticConditions.objects.all()
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

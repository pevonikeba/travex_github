from place.models import CLIMATE_CHOICES, HOW_COMFORTABLE_CHOICES, TypeTransport, Category, Transport, Place, \
    PlaceImage, MustSee, AccommodationOption, FloraFauna, ClimaticCondition, ClimaticConditiomm, GeographicalFeature
from django.db import models
from .serializers import TypeTransportSerializer, GeographicalFeatureSerializer
from .place_nested import CategorySerializer

from loguru import logger
from rest_framework import serializers


class FieldTypes:
    char_field = "char_field"
    text_field = "text_field"
    int_field = "int_field"
    float_field = "float_field"
    picker = "picker"
    image_field = "image_field"
    multi_select = "multi_select"
    multi_image_field = "multi_image_field"


def get_choices_options(choices: tuple):
    def from_tuple_to_dict(choice: tuple):
        return {
            "text": choice[1],
            "value": choice[0]
        }
    return map(from_tuple_to_dict, choices)


def get_model_options(Obj: models.Model, serializer, text_name_field='name'):
    def _transform_dict(obj):
        return {
            "text": obj[text_name_field],
            "value": obj["id"],
        }
    options = serializer(data=Obj.objects.all(), many=True)
    options.is_valid()
    return map(_transform_dict, options.data)


def get_is_field_required(model, field_name):
    return not model._meta.get_field(field_name).blank


def get_field_name(model, field_name):
    return model._meta.get_field(field_name).name


def get_plus_place():
    return [
    {
        "key": None,
        "header": "General Info",
        "is_nested": False,
        "inputs": [
            {
                "key": get_field_name(Place, 'name'),
                "placeholder": "Name",
                'title': 'Name',
                'field_type': FieldTypes.char_field,
                'required': get_is_field_required(Place, 'name'),
            },
            {
                "key": get_field_name(Place, 'nickname'),
                "placeholder": "Nickname",
                'title': 'Nickname',
                'field_type': FieldTypes.char_field,
                'required': get_is_field_required(Place, 'nickname'),
            },
            {
                "key": get_field_name(Place, 'description'),
                "placeholder": "Overview",
                'title': "Overview",
                'field_type': FieldTypes.text_field,
                'required': get_is_field_required(Place, 'description'),
            },
            # {
            #     "key": get_field_name(Place, 'rating'),
            #     "placeholder": "Rating",
            #     'title': "Rating",
            #     'field_type': FieldTypes.int_field,
            #     'required': get_is_field_required(Place, 'rating'),
            # }
        ]
    },
    {
        "key": get_field_name(Place, "place_images"),
        "header": "Images of place",
        "is_nested": True,
        "inputs": [
            {
                "key": get_field_name(PlaceImage, 'image'),
                'title': "Images",
                'field_type': FieldTypes.image_field,
                'required': get_is_field_required(PlaceImage, 'image'),
            },
        ]
    },
    {
        "key": None,
        "header": "Categories",
        "is_nested": False,
        "inputs": [
            {
                "key": get_field_name(Place, 'categories'),
                'title': 'Category',
                'field_type': FieldTypes.multi_select,
                "options": get_model_options(Category, CategorySerializer),
                'required': get_is_field_required(Place, 'categories'),
            },
        ]
    },
    {
        "key": None,
        "header": "Civilization",
        "is_nested": False,
        "inputs": [
            {
                'key': get_field_name(Place, "population"),
                "placeholder": "Population",
                'title': "Population",
                'field_type': FieldTypes.int_field,
                'required': get_is_field_required(Place, "population"),
            },
            {
                'key': get_field_name(Place, "type_of_people_around"),
                "placeholder": "Type Of People Around",
                'title': "Type Of People Around",
                'field_type': FieldTypes.text_field,
                'required': get_is_field_required(Place, "type_of_people_around"),
            },
            {
                'key': get_field_name(Place, "turist_rating"),
                "placeholder": "Turist Rating",
                'title': "Turist Rating",
                'field_type': FieldTypes.int_field,
                'required': get_is_field_required(Place, "turist_rating"),
            },
            {
                'key': get_field_name(Place, "nation"),
                "placeholder": "Nation",
                'title': "Nation",
                'field_type': FieldTypes.char_field,
                'required': get_is_field_required(Place, "nation"),
            },
            {
                'key': get_field_name(Place, "language"),
                "placeholder": "Language",
                'title': "Language",
                'field_type': FieldTypes.char_field,
                'required': get_is_field_required(Place, "language"),
            },
            {
                'key': get_field_name(Place, 'culture'),
                "placeholder": "Culture",
                'title': 'Culture',
                'field_type': FieldTypes.text_field,
                'required': get_is_field_required(Place, 'culture'),
            },
            {
                'key': get_field_name(Place, "currency"),
                "placeholder": "Currency",
                'title': "Currency",
                'field_type': FieldTypes.char_field,
                'required': get_is_field_required(Place, "currency"),
            },
            {
                'key': get_field_name(Place, 'currency_buying_advice'),
                "placeholder": "Currency Buying Advice",
                'title': 'Currency Buying Advice',
                'field_type': FieldTypes.text_field,
                'required': get_is_field_required(Place, 'currency_buying_advice'),
            },
            {
                'key': get_field_name(Place, "simcards"),
                "placeholder": "Sim Cards",
                'title': "Sim Cards",
                'field_type': FieldTypes.char_field,
                'required': get_is_field_required(Place, "simcards"),
            },
            {
                'key': get_field_name(Place, "internet"),
                "placeholder": "Internet",
                'title': "Internet",
                'field_type': FieldTypes.char_field,
                'required': get_is_field_required(Place, "internet"),
            },
            {
                'key': get_field_name(Place, 'pay_online_or_by_card'),
                "placeholder": "Payment Method",
                'title': 'Pay Online Or By Card',
                'field_type': FieldTypes.text_field,
                'required': get_is_field_required(Place, 'pay_online_or_by_card'),
            },
        ]
    },
    {
        "key": get_field_name(Place, "transports"),
        "header": "Transports",
        "is_nested": True,
        "inputs": [
            {
                "key": get_field_name(Transport, "type_transport"),
                "placeholder": "Type Of Transport",
                'title': 'Type Of Transport',
                'field_type': FieldTypes.picker,
                "options": get_model_options(TypeTransport, TypeTransportSerializer),
                'required': get_is_field_required(Transport, 'type_transport'),
            },
            {
                'key': get_field_name(Transport, "price"),
                "placeholder": "Transport Price",
                'title': "Transport Price",
                'field_type': FieldTypes.float_field,
                'required': get_is_field_required(Transport, 'price'),
            },
            {
                'key': get_field_name(Transport, "description"),
                "placeholder": "Transport Description",
                'title': "Transport Description",
                'field_type': FieldTypes.text_field,
                'required': get_is_field_required(Transport, "description"),
            },
            {
                'key': get_field_name(Transport, "comfortable"),
                "placeholder": "Transport Comfortable",
                'title': "Transport Comfortable",
                'field_type': FieldTypes.picker,
                "options": get_choices_options(HOW_COMFORTABLE_CHOICES),
                'required': get_is_field_required(Transport, "comfortable"),
            },
            {
                'key': get_field_name(Transport, 'image'),
                'title': "Transport Image",
                'field_type': FieldTypes.image_field,
                'required': get_is_field_required(Transport, 'image'),
            }
        ]
    },
        {
            "key": get_field_name(Place, "must_sees"),
            "header": "Must Sees",
            "is_nested": True,
            "inputs": [
                {
                    "key": get_field_name(MustSee, 'name'),
                    "placeholder": "Must See Name",
                    'title': 'Must See Name',
                    'field_type': FieldTypes.char_field,
                    'required': get_is_field_required(MustSee, 'name'),
                },
                {
                    'key': get_field_name(MustSee, 'description'),
                    "placeholder": "Description",
                    'title': "Description",
                    'field_type': FieldTypes.text_field,
                    'required': get_is_field_required(MustSee, 'description'),
                },
                {
                    'key': get_field_name(MustSee, 'image'),
                    'title': "Must See Image",
                    'field_type': FieldTypes.image_field,
                    'required': get_is_field_required(MustSee, 'image'),
                }
            ]
        },
        {
            "key": get_field_name(Place, 'accommodation_options'),
            "header": "Accommodation Options",
            "is_nested": True,
            "inputs": [
                {
                    "key": get_field_name(AccommodationOption, 'name'),
                    "placeholder": "Accommodation Options Name",
                    'title': 'Accommodation Options Name',
                    'field_type': FieldTypes.char_field,
                    'required': get_is_field_required(AccommodationOption, 'name'),
                },
                {
                    'key': get_field_name(AccommodationOption, 'price'),
                    "placeholder": "Price",
                    'title': "Price",
                    'field_type': FieldTypes.float_field,
                    'required': get_is_field_required(AccommodationOption, 'price'),
                },
                {
                    'key': get_field_name(AccommodationOption, 'description'),
                    "placeholder": "Description",
                    'title': "Description",
                    'field_type': FieldTypes.text_field,
                    'required': get_is_field_required(AccommodationOption, 'description'),
                },
            ]
        },
        {
            "key": get_field_name(Place, 'flora_faunas'),
            "header": "Flora and Fauna",
            "is_nested": True,
            "inputs": [
                {
                    "key": get_field_name(FloraFauna, 'name'),
                    "placeholder": "Flora and/or Fauna name",
                    'title': 'Flora and/or Fauna name',
                    'field_type': FieldTypes.char_field,
                    'required': get_is_field_required(FloraFauna, 'name'),
                },
                {
                    'key': get_field_name(FloraFauna, 'description'),
                    "placeholder": 'Description',
                    'title': "Description",
                    'field_type': FieldTypes.text_field,
                    'required': get_is_field_required(FloraFauna, 'description'),
                },
                {
                    'key': get_field_name(FloraFauna, 'image'),
                    'title': "Flora and Fauna Image",
                    'field_type': FieldTypes.image_field,
                    'required': get_is_field_required(FloraFauna, 'image'),
                }
            ]
        },
        {
            "key": get_field_name(Place, 'climatic_conditiomm'),
            "header": "Climate",
            "is_nested": False,
            "inputs": [
                {
                    "key": get_field_name(ClimaticConditiomm, 'condition'),
                    "placeholder": 'Condition',
                    'title': 'Condition',
                    'field_type': FieldTypes.text_field,
                    'required': get_is_field_required(ClimaticConditiomm, 'condition'),
                },
                {
                    "key": get_field_name(ClimaticConditiomm, 'climate'),
                    "placeholder": "Climate",
                    'title': "Climate",
                    'field_type': FieldTypes.picker,
                    "options": get_choices_options(CLIMATE_CHOICES),
                    'required': get_is_field_required(ClimaticConditiomm, 'climate'),
                },
                {
                    'key': get_field_name(ClimaticConditiomm, 'description'),
                    "placeholder": 'Description',
                    'title': "Description",
                    'field_type': FieldTypes.text_field,
                    'required': get_is_field_required(ClimaticConditiomm, 'description'),
                },
            ]
        },
        {
            'key': None,
            'header': 'Additional info',
            'is_nested': False,
            'inputs': [
                {
                    "key": get_field_name(Place, "nearest_airport"),
                    "placeholder": "Nearest Airport",
                    'title': 'Nearest Airport',
                    'field_type': FieldTypes.char_field,
                    'required': get_is_field_required(Place, "nearest_airport"),

                },
                {
                    'key': get_field_name(Place, "how_to_get_there"),
                    "placeholder": "How To Get There",
                    'title': "How To Get There",
                    'field_type': FieldTypes.text_field,
                    'required': get_is_field_required(Place, "how_to_get_there"),
                },
            ]
        },
        # {
        #     'key': get_field_name(Place, 'geographical_feature'),
        #     'header': 'Geographical feature',
        #     'is_nested': False,
        #     "placeholder": "Geographical feature",
        #     'title': 'Geographical feature',
        #     'field_type': FieldTypes.picker,
        #     "options": get_model_options(GeographicalFeature, GeographicalFeatureSerializer, '__str__'),
        #     'required': get_is_field_required(Place, 'geographical_feature'),
        #     # 'inputs': [
        #
        #     # ]
        # }
]


nested = [
     {
         "header": "Climate",
         "key": None,
         "is_nested": False,
         "inputs": [
             {
                 "placeholder": "Climate",
                 'title': 'Climate',
                 'key': 'climatic_condition',
                 'field_type': FieldTypes.picker,
                 "options":  [
                    {"text": 'Tropical', "value": 1, },
                    {"text": 'Dry', "value": 1, },
                    {"text": 'Mild', "value": 1, },
                    {"text": 'Continental', "value": 1, },
                    {"text": 'Polar', "value": 1, },
                    ],
                 'required': True,
             },
         ]
     },
    {
        "header": "Geographical Feature",
        'key': None,
        "is_nested": False,
        "inputs": [
            {
                "placeholder": "Geographical Feature",
                'title': 'Geographical Feature',
                'key': 'geographical_feature',
                'field_type': FieldTypes.char_field,
                'required': False,
            },
            {
                "placeholder": "Geographical Feature Description",
                'title': 'Geographical Feature Description',
                'key': 'geographical_feature_description',
                'field_type': FieldTypes.char_field,
                'required': False,
            },
        ]
    },
    {
        # TODO: header nuzhno pridumat cto by oharektezowala children
        "header": "---------------------------------------------------------------------------------------------------------------------------------------------------------------------",
        "key": None,
        "is_nested": False,
        "inputs": [

        ]
    },
    {
        "header": "Cuisine",
        "key": "cuisines",
        "is_nested": True,
        "inputs": [
            {
                "placeholder": "Kind Of Cuisine",
                'title': 'Kind Of Cuisine',
                "key": "name",
                'field_type': FieldTypes.picker,
                "options": [
                    {"text": 'French Cuisine', "value": 'French Cuisine', },
                    {"text": 'Chinese Cuisine', "value": 'Chinese Cuisine', },
                    {"text": 'Japanese Cuisine', "value": 'Japanese Cuisine', },
                    {"text": 'Indian Cuisine', "value": 'Indian Cuisine', },
                    {"text": 'Italian Cuisine', "value": 'Italian Cuisine', },
                    {"text": 'Greek Cuisine', "value": 'Greek Cuisine', },
                    {"text": 'Spanish Cuisine', "value": 'Spanish Cuisine', },
                    {"text": 'Mediterranean Cuisine', "value": 'Mediterranean Cuisine', },
                ],
                'required': False,
            },
            {
                "placeholder": "Cuisine Price",
                'title': "Cuisine Price",
                'key': "price",
                'field_type': FieldTypes.float_field,
                'required': False,
            },
            {
                "placeholder": "Transport Description",
                'title': "Transport Description",
                'key': "description",
                'field_type': FieldTypes.text_field,
                'required': False,
            },
            {
                'title': "Cuisine Image",
                'key': 'image',
                'field_type': FieldTypes.image_field,
                'required': False,
            }
        ]
    },
    {
        "header": "Safe",
        "key": "safe",
        "is_nested": True,
        "inputs": [
            {
                "placeholder": "Safe Name",
                'title': 'Safe Name',
                "key": "name",
                'field_type': FieldTypes.char_field,
                'required': False,
            },
            {
                "placeholder": "How Dangerous",
                'title': "How Dangerous",
                'key': "how_dangerous",
                'field_type': FieldTypes.picker,
                "options": [
                    {"text": 'Very Safe', "value": 1, },
                    {"text": 'Safe', "value": 1, },
                    {"text": 'Average', "value": 1, },
                    {"text": 'Somewhat Dangerous', "value": 1, },
                    {"text": 'Dangerous', "value": 1, },
                ],
                'required': False,
            },
            {
                "placeholder": "Rating Danger",
                'title': "Rating Danger",
                'key': "rating_danger",
                'field_type': FieldTypes.int_field,
                'required': False,
            },
            {
                "placeholder": "Description",
                'title': "Description",
                'key': 'description',
                'field_type': FieldTypes.text_field,
                'required': False,
            }
        ]
    },
    {
        "header": "Entertainment",
        "key": "entertainment",
        "is_nested": True,
        "inputs": [
            {
                "placeholder": "Entertainment Name",
                'title': 'Entertainment Name',
                "key": "name",
                'field_type': FieldTypes.char_field,
                'required': False,
            },
            {
                "placeholder": "Description",
                'title': "Description",
                'key': 'description',
                'field_type': FieldTypes.text_field,
                'required': False,
            },
            {
                'title': "Cuisine Image",
                'key': 'image',
                'field_type': FieldTypes.image_field,
                'required': False,
            }
        ]
    },
    {
        "header": "Natural Phenomena",
        "key": "natural_phenomena",
        "is_nested": True,
        "inputs": [
            {
                "placeholder": "Natural Phenomena Name",
                'title': 'Natural Phenomena Name',
                "key": "name",
                'field_type': FieldTypes.char_field,
                'required': False,
            },
            {
                "placeholder": "Description",
                'title': "Description",
                'key': 'description',
                'field_type': FieldTypes.text_field,
                'required': False,
            },
            {
                'title': "Cuisine Image",
                'key': 'image',
                'field_type': FieldTypes.image_field,
                'required': False,
            }
        ]
    },

    {
        "header": "Uniqueness Place",
        "key": "uniqueness_place",
        "is_nested": True,
        "inputs": [
            {
                "placeholder": "Uniqueness Place Name",
                'title': 'Uniqueness Place Name',
                "key": "name",
                'field_type': FieldTypes.char_field,
                'required': True,
            },
            {
                "placeholder": "Description",
                'title': "Description",
                'key': 'description',
                'field_type': FieldTypes.text_field,
                'required': True,
            },
            {
                'title': "Uniqueness Place Image",
                'key': 'image',
                'field_type': FieldTypes.image_field,
                'required': False,
            }
        ]
    },

    {
        "header": "Vibe",
        "key": "vibe",
        "is_nested": True,
        "inputs": [
            {
                "placeholder": "Vibe Name",
                'title': 'Vibe Name',
                "key": "name",
                'field_type': FieldTypes.char_field,
                'required': False,
            },
            {
                'title': "Vibe Image",
                'key': 'image',
                'field_type': FieldTypes.image_field,
                'required': False,
            }
        ]
    },
    {
        "header": "Where To Take A Picture",
        "key": "where_to_take_a_picture",
        "is_nested": True,
        "inputs": [
            {
                "placeholder": "Where To Take A Picture Name",
                'title': 'Where To Take A Picture Name',
                "key": "name",
                'field_type': FieldTypes.char_field,
                'required': False,
            },
            {
                "placeholder": "Description",
                'title': "Description",
                'key': 'description',
                'field_type': FieldTypes.text_field,
                'required': False,
            },
            {
                'title': "Where To Take A Picture Image",
                'key': 'image',
                'field_type': FieldTypes.image_field,
                'required': False,
            }

        ]
    },
    {
        "header": "Interesting Facts",
        "key": "interesting_fact",
        "is_nested": True,
        "inputs": [
            {
                "placeholder": "Description",
                'title': "Description",
                'key': 'description',
                'field_type': FieldTypes.text_field,
                'required': False,
            },
            {
                'title': "Interesting Facts Image",
                'key': 'image',
                'field_type': FieldTypes.image_field,
                'required': False,
            }

        ]
    },

    {
        "header": "Practical Information",
        "key": "practical_information",
        "is_nested": True,
        "inputs": [
            {
                "placeholder": "Description",
                'title': "Description",
                'key': 'description',
                'field_type': FieldTypes.text_field,
                'required': False,
            },
        ]
    },
]



category_choices = (
    {"text": 'Active', "value": 1, },
    {"text": 'Adventures', "value": 2, },
    {"text": 'Alien', "value": 3, },
    {"text": 'Animal', "value": 4, },
    {"text": 'Cinema', "value": 5, },
    {"text": 'Cultural', "value": 6, },
    {"text": 'Digging', "value": 7, },
    {"text": 'Eco', "value": 8, },
    {"text": 'Event', "value": 9, },
    {"text": 'Exotic', "value": 10, },
    {"text": 'Extreme', "value": 11, },
    {"text": 'Family', "value": 12, },
    {"text": 'From 7 d', "value": 13, },
    {"text": 'Gastro', "value": 14, },
    {"text": 'Gothic', "value": 15, },
    {"text": 'Jailoo', "value": 16, },
    {"text": 'Mystery', "value": 17, },
    {"text": 'Philosophy', "value": 18, },
    {"text": 'Recreation', "value": 19, },
    {"text": 'Pilgrimage', "value": 20, },
    {"text": 'Spirit', "value": 21, },
    {"text": 'Up to 3', "value": 22, },
    {"text": 'Up to 7 d', "value": 23, },
    {"text": 'Honeymoon', "value": 24, },
    {"text": 'Urban', "value": 25, },
    {"text": 'Welness', "value": 26, },
)
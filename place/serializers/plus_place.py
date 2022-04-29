from place.models import CLIMATE_CHOICES, HOW_COMFORTABLE_CHOICES, TypeTransport
from django.db import models
from .serializers import TypeTransportSerializer

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
            {
                "placeholder": "Nearest Airport",
                'title': 'Nearest Airport',
                "key": "nearest_airport",
                'field_type': FieldTypes.char_field,
                'required': False,

            },
            {
                "placeholder": "How To Get There",
                'title': "How To Get There",
                'key': "how_to_get_there",
                'field_type': FieldTypes.text_field,
                'required': True,
            },
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
        "header": "Accommodation Option",
        "key": "accommodation_option",
        "is_nested": True,
        "inputs": [
            {
                "placeholder": "Accommodation Options Name",
                'title': 'Accommodation Options Name',
                "key": "name",
                'field_type': FieldTypes.char_field,
                'required': False,
            },
            {
                "placeholder": "Price",
                'title': "Price",
                'key': "price",
                'field_type': FieldTypes.float_field,
                'required': False,
            },
            {
                "placeholder": "Description",
                'title': "Description",
                'key': 'description',
                'field_type': FieldTypes.text_field,
                'required': False,
            },
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
        "header": "Must See",
        "key": "must_see",
        "is_nested": True,
        "inputs": [
            {
                "placeholder": "Must See Name",
                'title': 'Must See Name',
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
                'title': "Must See Image",
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
    {
        "header": "FloraAndFauna",
        "key": "flora_fauna",
        "is_nested": True,
        "inputs": [
            {
                "placeholder": "FloraAndFauna Name",
                'title': 'FloraAndFauna Name',
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
                'title': "FloraAndFauna Image",
                'key': 'image',
                'field_type': FieldTypes.image_field,
                'required': False,
            }
        ]
    },
]


def get_choices_options(choices: tuple):
    def from_tuple_to_dict(choice: tuple):
        return {
            "text": choice[1],
            "value": choice[0]
        }
    return map(from_tuple_to_dict, choices)


def get_model_options(Obj: models.Model, serializer):
    def _transform_dict(obj):
        return {
            "text": obj["name"],
            "value": obj["id"],
        }
    options = serializer(data=Obj.objects.all(), many=True)
    options.is_valid()
    return map(_transform_dict, options.data)


def get_plus_place():
    return [
    {
        "header": "General Info",
        "key": None,
        "is_nested": False,
        "inputs": [
            {
                "placeholder": "Name",
                'title': 'Name',
                "key": 'name',
                'field_type': FieldTypes.char_field,
                'required': True,
            },
            {
                "placeholder": "Nickname",
                'title': 'Nickname',
                "key": 'nickname',
                'field_type': FieldTypes.char_field,
                'required': False,
            },
            {
                "placeholder": "Overview",
                'title': "Overview",
                "key": 'description',
                'field_type': FieldTypes.text_field,
                'required': False,
            },
            {
                "placeholder": "Rating",
                'title': "Rating",
                "key": 'rating',
                'field_type': FieldTypes.int_field,
                'required': False,
            }
        ]
    },
    {
        "header": "Images",
        "key": None,
        "is_nested": False,
        "inputs": [
            {
                'title': "Images",
                "key": 'place_images',
                'field_type': FieldTypes.multi_image_field,
                'required': True,
            },

        ]
    },
    {
        "header": "Category",
        "key": None,
        "is_nested": False,
        "inputs": [
            {
                'title': 'Category',
                "key": 'categories',
                'field_type': FieldTypes.multi_select,
                "options": [
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
                ],
                'required': True,
            },
        ]
    },
    {
        "header": "Civilization",
        "key": None,
        "is_nested": False,
        "inputs": [
            {
                "placeholder": "Population",
                'title': "Population",
                'key': "population",
                'field_type': FieldTypes.int_field,
                'required': False,
            },
            {
                "placeholder": "Type Of People Around",
                'title': "Type Of People Around",
                'key': "type_of_people_around",
                'field_type': FieldTypes.text_field,
                'required': False,
            },
            {
                "placeholder": "Turist Rating",
                'title': "Turist Rating",
                'key': "turist_rating",
                'field_type': FieldTypes.int_field,
                'required': False,
            },
            {
                "placeholder": "Nation",
                'title': "Nation",
                'key': "nation",
                'field_type': FieldTypes.char_field,
                'required': False,
            },
            {
                "placeholder": "Language",
                'title': "Language",
                'key': "language",
                'field_type': FieldTypes.char_field,
                'required': False,
            },
            {
                "placeholder": "Culture",
                'title': 'Culture',
                'key': 'culture',
                'field_type': FieldTypes.text_field,
                'required': False,
            },
            {
                "placeholder": "Currency",
                'title': "Currency",
                'key': "currency",
                'field_type': FieldTypes.char_field,
                'required': False,
            },
            {
                "placeholder": "Currency Buying Advice",
                'title': 'Currency Buying Advice',
                'key': 'currency_buying_advice',
                'field_type': FieldTypes.text_field,
                'required': False,
            },
            {
                "placeholder": "Sim Cards",
                'title': "Sim Cards",
                'key': "simcards",
                'field_type': FieldTypes.char_field,
                'required': False,
            },
            {
                "placeholder": "Internet",
                'title': "Internet",
                'key': "internet",
                'field_type': FieldTypes.char_field,
                'required': False,
            },
            {
                "placeholder": "Payment Method",
                'title': 'Pay Online Or By Card',
                'key': 'pay_online_or_by_card',
                'field_type': FieldTypes.text_field,
                'required': False,
            },
        ]
    },
    {
        "header": "Transport",
        "key": "transports",
        "is_nested": True,
        "inputs": [
            {
                "placeholder": "Kind Of Transport",
                'title': 'Kind Of Transport',
                "key": "type_transport",
                'field_type': FieldTypes.picker,
                "options": get_model_options(TypeTransport, TypeTransportSerializer),
                'required': False,
            },
            {
                "placeholder": "Transport Price",
                'title': "Transport Price",
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
                "placeholder": "Transport Comfortable",
                'title': "Transport Comfortable",
                'key': "comfortable",
                'field_type': FieldTypes.picker,
                "options": get_choices_options(HOW_COMFORTABLE_CHOICES),
                'required': False,
            },
            {
                'title': "Transport Image",
                'key': 'image',
                'field_type': FieldTypes.image_field,
                'required': False,
            }
        ]
    },
]

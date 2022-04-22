
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
        "key": None,

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
        "header": "Accommodation Option",
        "key": "accommodation_option",
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

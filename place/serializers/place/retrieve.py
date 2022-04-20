from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

from place.models import Place, Image

{
"sections": [
                {
                    "children": [
                        {
                            "id": 1,
                            "description": "<p>Continent: asia</p><p>Country: JP</p><p>region: region</p><p>City: city</p><p>Latitude: 24.2500000000</p><p>Longitude: 23.2300000000</p><p>nearest_place: nearest place</p>"
                        }
                    ],
                    "title": "Locations",
                    "key": "locations",
                    "display_type": "drop_down"
                },
                {
                    "children": [
                        {
                            "id": 1,
                            "description": "<h1>type name</h1><img src=/media/images/authentic.webp/><p>Price: 3245.00</p><p>Comfortable: comfortable</p><p>asdgasdgasdg sd fsad a</p>"
                        }
                    ],
                    "title": "Transports",
                    "key": "transports",
                    "display_type": "drop_down"
                },
                {
                    "children": [
                        {
                            "id": 1,
                            "description": "<h1>sdgasg</h1><p>Price: 10.00</p><p>sklahguhs</p>"
                        }
                    ],
                    "title": "Accommodationoptions",
                    "key": "accommodationoptions",
                    "display_type": "drop_down"
                },
                {
                    "children": [
                        {
                            "id": 1,
                            "description": "<h1>sdgas</h1><img src=/media/images/medical_and_health_miracle.jpeg/><p>ashasd asgas dg asdhas h ash</p>"
                        }
                    ],
                    "title": "Must see",
                    "key": "must_see",
                    "display_type": "drop_down"
                },
                {
                    "children": [
                        {
                            "id": 1,
                            "description": "<h1>sdgs sd</h1><img src=/media/images/lafoten_tukan.jpeg/><p>g sag as gsd ga</p>"
                        }
                    ],
                    "title": "Where to take a picture",
                    "key": "where_to_take_a_picture",
                    "display_type": "drop_down"
                },
                {
                    "children": [
                        {
                            "id": 1,
                            "description": "<h1>asdg</h1><img src=/media/images/culture_historical__kslnLE2.jpeg/><p>Price: 324.00</p><p>asdgksdjgj as</p>"
                        }
                    ],
                    "title": "Cuisines",
                    "key": "cuisines",
                    "display_type": "drop_down"
                },
                {
                    "children": [
                        {
                            "id": 1,
                            "description": "<h1>safe name</h1><p>How Dangerous: somewhat dangerous</p><p>Rating Danger: 4</p><p>safe description</p>"
                        }
                    ],
                    "title": "Safes",
                    "key": "safes",
                    "display_type": "drop_down"
                },
                {
                    "children": [
                        {
                            "id": 1,
                            "description": "<h1>gsdgasdg s</h1><img src=/media/images/sports_and_extreme_recreation.jpeg/><p>jh dslsh dhf as</p>"
                        }
                    ],
                    "title": "Natural phenomena",
                    "key": "natural_phenomena",
                    "display_type": "drop_down"
                },
                {
                    "vibe": "sdgas",
                    "children": [
                        {
                            "id": 1,
                            "description": "<img src=/media/images/pilgrimage.webp/>"
                        }
                    ],
                    "title": "Vibes",
                    "key": "vibes",
                    "display_type": "drop_down"
                },
                {
                    "children": [
                        {
                            "id": 1,
                            "description": "<img src=/media/images/wise_space_to_philosophize.jpeg/><p>skahslkjd sdf asjf;laks</p>"
                        }
                    ],
                    "title": "Interesting facts",
                    "key": "interesting_facts",
                    "display_type": "drop_down"
                },
                {
                    "children": [
                        {
                            "id": 1,
                            "description": "<p>sdgjshd ljfhasjdhfl asdhfjas fa</p>"
                        },
                        {
                            "id": 2,
                            "description": "<p>alksdnfahsndkfnas;kl dfa</p>"
                        },
                        {
                            "id": 3,
                            "description": "<p>asdjfkljsad;lfj asmkldf</p>"
                        }
                    ],
                    "title": "Practical informations",
                    "key": "practical_informations",
                    "display_type": "drop_down"
                },
                {
                    "children": [
                        {
                            "id": 1,
                            "description": "<h1>lahs udhgf iuashd fkjsa dfk a</h1><img src=/media/images/adventure_spirit_SUDzMPj.jpeg/><p>h asljd hfashdfkhasdfjalsjdf ashdfjasdf kas;dfk a</p>"
                        },
                        {
                            "id": 2,
                            "description": "<h1>sdh asjdnfn s</h1><img src=/media/images/treasure_of_fauna_and_flora.jpeg/><p>s dngans;d kg;hna;skdmng a</p>"
                        }
                    ],
                    "title": "Flora fauna",
                    "key": "flora_fauna",
                    "display_type": "grid"
                }
            ]
}

class ImageSerializer(serializers.ModelSerializer):
    # path = Base64ImageField()  # From DRF Extra Fields
    class Meta:
        model = Image
        fields = ('id', 'path',)


class PlaceRetrieveSerializer(serializers.ModelSerializer):
    sections = serializers.SerializerMethodField()
    images = ImageSerializer(many=True, required=False)

    class Meta:
        model = Place
        fields = ('id', 'images', 'rating', 'location', 'writer_user', 'sections',)
        # depth = 1

    # def create

    def get_sections(self, obj):
        return [
            {
                "key": "overview",
                "title": "Overview",
                "display_type": "drop_down",
                "children": {
                    "id": 1,
                    "title": "overview.name",
                    "description": "<p>dfgdsfg</p>"
                },
            },
        ]

    def get_overview(self, obj):
        return {
            "name": obj.name,
            "description": obj.description,
        }





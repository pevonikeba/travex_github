from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

from place.models import Place, Image, Transport, AccommodationOption, MustSee, FloraFauna
from loguru import logger


{
"sections": [
                {
                    "children": [
                        {
                            "id": 1,
                            "title": "",
                            "description": "<p>Continent: asia</p><p>Country: Nigeria</p><p>region: Kebbi</p><p>City: Waje</p><p>Latitude: 11.5516225000</p><p>Longitude: 5.4981583000</p><p>nearest_place: nearest place</p>"
                        }
                    ],
                    "title": "Location",
                    "key": "location",
                    "icon_name": "article",
                    "display_type": "drop_down"
                },
                {
                    "children": [
                        {
                            "id": 1,
                            "title": "<h1>type name</h1>",
                            "description": "<img src=/media/images/authentic.webp/><p>Price: 3245.00</p><p>Comfortable: comfortable</p><p>asdgasdgasdg sd fsad a</p>"
                        }
                    ],
                    "title": "Transport",
                    "key": "transport",
                    "icon_name": "article",
                    "display_type": "drop_down"
                },
                {
                    "children": [
                        {
                            "id": 1,
                            "title": "<h1>sdgasg</h1>",
                            "description": "<p>Price: 10.00</p><p>sklahguhs</p>"
                        }
                    ],
                    "title": "Accommodation option",
                    "key": "accommodation_option",
                    "icon_name": "article",
                    "display_type": "drop_down"
                },
                {
                    "children": [
                        {
                            "id": 1,
                            "title": "<h1>sdgas</h1>",
                            "description": "<img src=/media/images/medical_and_health_miracle.jpeg/><p>ashasd asgas dg asdhas h ash</p>"
                        }
                    ],
                    "title": "Must see",
                    "key": "must_see",
                    "icon_name": "article",
                    "display_type": "drop_down"
                },
                {
                    "children": [
                        {
                            "id": 1,
                            "title": "<h1>sdgs sd</h1>",
                            "description": "<img src=/media/images/lafoten_tukan.jpeg/><p>g sag as gsd ga</p>"
                        }
                    ],
                    "title": "Where to take a picture",
                    "key": "where_to_take_a_picture",
                    "icon_name": "article",
                    "display_type": "drop_down"
                },
                {
                    "children": [
                        {
                            "id": 1,
                            "title": "<h1>asdg</h1>",
                            "description": "<img src=/media/images/culture_historical__kslnLE2.jpeg/><p>Price: 324.00</p><p>asdgksdjgj as</p>"
                        }
                    ],
                    "title": "Cuisine",
                    "key": "cuisine",
                    "icon_name": "article",
                    "display_type": "drop_down"
                },
                {
                    "children": [
                        {
                            "id": 1,
                            "title": "<h1>gsdgasdg s</h1>",
                            "description": "<img src=/media/images/sports_and_extreme_recreation.jpeg/><p>jh dslsh dhf as</p>"
                        }
                    ],
                    "title": "Natural phenomena",
                    "key": "natural_phenomena",
                    "icon_name": "article",
                    "display_type": "drop_down"
                },
                {
                    "children": [
                        {
                            "id": 1,
                            "title": "<h1>sdgas</h1>",
                            "description": "<img src=/media/images/pilgrimage.webp/>"
                        }
                    ],
                    "title": "Vibe",
                    "key": "vibe",
                    "icon_name": "article",
                    "display_type": "drop_down"
                },
                {
                    "children": [
                        {
                            "id": 1,
                            "title": "",
                            "description": "<img src=/media/images/wise_space_to_philosophize.jpeg/><p>skahslkjd sdf asjf;laks</p>"
                        }
                    ],
                    "title": "Interesting fact",
                    "key": "interesting_fact",
                    "icon_name": "article",
                    "display_type": "drop_down"
                },
                {
                    "children": [
                        {
                            "id": 1,
                            "title": "",
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
                    "title": "Practical information",
                    "key": "practical_information",
                    "icon_name": "article",
                    "display_type": "drop_down"
                },
                {
                    "children": [
                        {
                            "id": 1,
                            "title": "<h1>lahs udhgf iuashd fkjsa dfk a</h1>",
                            "description": "<img src=/media/images/adventure_spirit_SUDzMPj.jpeg/><p>h asljd hfashdfkhasdfjalsjdf ashdfjasdf kas;dfk a</p>"
                        },
                        {
                            "id": 2,
                            "description": "<h1>sdh asjdnfn s</h1><img src=/media/images/treasure_of_fauna_and_flora.jpeg/><p>s dngans;d kg;hna;skdmng a</p>"
                        }
                    ],
                    "title": "Flora fauna",
                    "key": "flora_fauna",
                    "icon_name": "article",
                    "display_type": "grid"
                }
            ]
}


# class TransportSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Transport
#         fields = ('id', 'type_transport', 'price', 'description', 'comfortable', 'image',)

class ImageSerializer(serializers.ModelSerializer):
    # path = serializers.SerializerMethodField()
    # full_url = serializers.SerializerMethodField()


    class Meta:
        model = Image
        fields = ('id', 'path', )

    # def get_full_url(self, car):
    #     request = self.context.get('request')
    #     photo_url = car.url
    #     return request.build_absolute_uri(photo_url)

    # def get_path(self, obj):
    #     return obj.path


def create_section(obj: Place, key: str, icon_name: str, display_type: str, create_children):
    return {
            "title": key.capitalize(),
            "key": key,
            "icon_name": icon_name,
            "display_type": display_type,
            "children": create_children(obj, key),
        }


class PlaceRetrieveSerializer(serializers.ModelSerializer):
    sections = serializers.SerializerMethodField()
    images = ImageSerializer(many=True, required=False)

    class Meta:
        model = Place
        fields = ('id', 'images', 'rating', 'location', 'writer_user', 'sections',)
        # depth = 1

    def create_full_img_url(self, url):
        return self.context.get('request').build_absolute_uri(url)

    def create_p_tag(self, key, value):
        return f"<p>{key}: {value}</p>"

    def create_img_tag(self, url):
        full_img_url = self.create_full_img_url(url)
        return f"<img src={full_img_url}/>"

    def transport_children(self, obj: Place, key: str):
        def create_children(trans: Transport):
            price = self.create_p_tag("Price", trans.price)
            # TODO: add to img "media/" prefix
            img = self.create_img_tag(self.context.get('request').build_absolute_uri(trans.image.url))
            comfortable = self.create_p_tag("Comfortable", trans.comfortable)
            description = trans.description
            return {
                        "id": trans.pk,
                        "title": trans.type_transport.name,
                        "description": f"{img}{price}{comfortable}{description}",
                        "img": None,
                    }

        return map(create_children, getattr(obj, key).all())

    def accommodation_option_children(self, obj: Place, key: str):
        def create_children(ao: AccommodationOption):
            price = self.create_p_tag("Price", ao.price)
            description = ao.description
            return {
                        "id": ao.pk,
                        "title": ao.name,
                        "description": f"{price}{description}",
                        "img": None,
                    }

        return map(create_children, getattr(obj, key).all())

    def must_see_children(self, obj: Place, key: str):
        def create_children(ms: MustSee):
            img = self.create_img_tag(ms.image.url)
            description = ms.description
            return {
                "id": ms.pk,
                "title": ms.name,
                "description": f"{img}{description}",
                "img": None,
            }

        return map(create_children, getattr(obj, key).all())

    def flora_fauna_children(self, obj: Place, key: str):
        def create_children(ff: FloraFauna):
            img = self.create_img_tag(ff.image.url)
            description = ff.description
            return {
                "id": ff.pk,
                "title": ff.name,
                "description": f"{img}{description}",
                "img": self.create_full_img_url(ff.image.url),
            }

        return map(create_children, getattr(obj, key).all())

    def get_sections(self, obj: Place):
        return [
            create_section(
                key="transport",
                obj=obj,
                icon_name="directions",
                display_type="drop_down",
                create_children=self.transport_children,
            ),
            create_section(
                key="accommodation_option",
                obj=obj,
                icon_name="bed",
                display_type="drop_down",
                create_children=self.accommodation_option_children,
            ),
            create_section(
                key="must_see",
                obj=obj,
                icon_name="article",
                display_type="drop_down",
                create_children=self.must_see_children,
            ),
            create_section(
                key="flora_fauna",
                obj=obj,
                icon_name="article",
                display_type="grid",
                create_children=self.flora_fauna_children,
            ),

        ]






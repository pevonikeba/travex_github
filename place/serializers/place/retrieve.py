# from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

from place.models import Place, PlaceImage, Transport, AccommodationOption, MustSee, FloraFauna
from place.serializers.serializers import CustomUserSerializer
from loguru import logger

from place.serializers.place_nested import PlaceImageSerializer


a = {
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

class IconNames:
    article = 'article'
    bed = 'bed'
    people = 'people'
    cloud = 'cloud'
    restaurant_menu = 'restaurant_menu'
    attractions_rounded = 'attractions_rounded'
    grass = 'grass'
    done = 'done'
    star = 'star'
    lock = 'lock'
    terrain = 'terrain'
    directions = 'directions'
    camera = 'camera'
    surfing = 'surfing'


class PlaceOnAddDeleteBookmarkLikeSerializer(serializers.ModelSerializer):
    is_bookmarked = serializers.SerializerMethodField()

    class Meta:
        model = Place
        fields = ('id', 'is_bookmarked', )

    def is_bookmark_like(self, obj, attr_name):
        request = self.context.get('request')
        if getattr(obj, attr_name).filter(pk=request.user.id).exists():
            return True
        return False

    def get_is_bookmarked(self, obj: Place):
        return self.is_bookmark_like(obj, 'bookmarked_users')


def create_section_nested(obj: Place, key: str, icon_name: str, display_type: str, create_children):
    children = getattr(obj, key)
    if not children.exists():
        return {}
    return {
        "title": key.capitalize(),
        "key": key,
        "icon_name": icon_name,
        "display_type": display_type,
        "children": map(create_children, children.all()),
    }


def create_section_simple(title, key, icon_name, display_type, children):
    has_description = False
    for child in children:
        if child['description'].strip() != '':
            has_description = True
    if not has_description:
        return {}
    return {
        "title": title,
        "key": key,
        "icon_name": icon_name,
        "display_type": display_type,
        "children": children,
    },


class PlaceRetrieveSerializer(serializers.ModelSerializer):
    sections = serializers.SerializerMethodField()
    place_images = PlaceImageSerializer(many=True, required=False)
    writer_user = CustomUserSerializer(default=serializers.CurrentUserDefault())
    is_bookmarked = serializers.SerializerMethodField()
    is_wowed = serializers.SerializerMethodField()
    is_nahed = serializers.SerializerMethodField()
    wows_count = serializers.SerializerMethodField()
    nahs_count = serializers.SerializerMethodField()

    class Meta:
        model = Place
        fields = ('id', 'place_images',
                  'is_bookmarked', 'is_wowed', 'is_nahed',
                  'wows_count', 'nahs_count',
                  'locations', 'writer_user', 'sections', 'categories',)
        # depth = 1

    def get_wows_count(self, obj: Place):
        return obj.wowed_users.all().count()

    def get_nahs_count(self, obj: Place):
        return obj.nahed_users.all().count()

    def is_bookmark_like(self, obj, attr_name):
        request = self.context.get('request')
        if getattr(obj, attr_name).filter(pk=request.user.id).exists():
            return True
        return False

    def get_is_bookmarked(self, obj: Place):
        return self.is_bookmark_like(obj, 'bookmarked_users')

    def get_is_wowed(self, obj: Place):
        return self.is_bookmark_like(obj, 'wowed_users')

    def get_is_nahed(self, obj:Place):
        return self.is_bookmark_like(obj, 'nahed_users')

    # def get_is_bookmarked(self, obj: Place):
    #     request = self.context.get('request')
    #     if obj.bookmarked_users.filter(pk=request.user.id).exists():
    #         return True
    #     return False

    def create_full_img_url(self, url: str):
        return self.context.get('request').build_absolute_uri(url)

    def create_p_tag(self, key: str, value: str):
        if not value or value == 'None':
            return ""
        return f"<p>{key}: {value}</p>"

    def create_img_tag(self, url: str):
        if url is None:
            return ""
        full_img_url = self.create_full_img_url(url)
        return f"<img src={full_img_url}/>"

    # def place_images_children(self, place_image: PlaceImage):

    def transport_children(self, trans: Transport):
        img = self.create_img_tag(trans.image.url) if trans.image else ""
        price = self.create_p_tag("Price", trans.price)
        comfortable = self.create_p_tag("Comfortable", trans.comfortable)
        description = self.create_p_tag("Description", trans.description)
        return {
            "id": trans.pk,
            "title": trans.type_transport.name,
            "description": f"{img}{price}{comfortable}{description}",
            "image": None,
        }

    def accommodation_option_children(self, ao: AccommodationOption):
        price = self.create_p_tag("Price", ao.price)
        description = self.create_p_tag("Description", ao.description)
        return {
            "id": ao.pk,
            "title": ao.name,
            "description": f"{price}{description}",
            "image": None,
        }

    def must_see_children(self, ms: MustSee):
        img = self.create_img_tag(ms.image.url) if ms.image else ""
        description = self.create_p_tag("Description", ms.description)
        return {
            "id": ms.pk,
            "title": ms.name,
            "description": f"{img}{description}",
            "image": None,
        }

    def flora_fauna_children(self, ff: FloraFauna):
        img = self.create_img_tag(ff.image.url) if ff.image else ""
        description = self.create_p_tag("Description", ff.description)
        return {
            "id": ff.pk,
            "title": ff.name,
            "description": f"{img}{description}",
            "image": self.create_full_img_url(ff.image.url),
        }

    def general_info_description(self, place: Place):
        name = self.create_p_tag('Name', place.name)
        nickname = self.create_p_tag('Nickname', place.nickname)
        description = self.create_p_tag('Description', place.description)
        return f'{name}{nickname}{description}'

    def civilization_description(self, place: Place):
        population = self.create_p_tag('Population', str(place.population))
        type_of_people_around = self.create_p_tag('Type of people around', place.type_of_people_around)
        turist_rating = self.create_p_tag('Turist rating', place.turist_rating)
        nation = self.create_p_tag('Nation', place.nation)
        language = self.create_p_tag('Language', place.language)
        culture = self.create_p_tag('Culture', place.culture)
        currency = self.create_p_tag('Currency', place.currency)
        currency_buying_advice = self.create_p_tag('Currency buying advice', place.currency_buying_advice)
        simcards = self.create_p_tag('Simcards', place.simcards)
        internet = self.create_p_tag('Internet', place.internet)
        pay_online_or_by_card = self.create_p_tag('Pay online or by card', place.pay_online_or_by_card)

        return f'{population}{type_of_people_around}{turist_rating}{nation}{language}' \
               f'{culture}{currency}{currency_buying_advice}{simcards}{internet}{pay_online_or_by_card}'

    def climatic_condition_description(self, place: Place):
        climatic_condition = place.climatic_condition
        if not climatic_condition:
            return ''
        condition = self.create_p_tag('Condition', climatic_condition.condition)
        climate = self.create_p_tag('Climate', climatic_condition.climate)
        description = self.create_p_tag('Description', climatic_condition.description)

        return f'{condition}{climate}{description}'

    def geographical_feature_description(self, place: Place):
        geographical_feature = place.geographical_feature
        if not geographical_feature:
            return ''
        types_of_ecosystem = self.create_p_tag('Types of ecosystem', geographical_feature.types_of_ecosystem)
        types_of_ecosystem_description = self.create_p_tag('Types of ecosystem description',
                                                           geographical_feature.types_of_ecosystem_description)
        description = self.create_p_tag('Description', geographical_feature.description)

        return f'{types_of_ecosystem}{types_of_ecosystem_description}{description}'

    def nearest_airport_description(self, place: Place):
        nearest_airport = self.create_p_tag('Nearest airport', place.nearest_airport)
        return f'{nearest_airport}'

    def how_to_get_there_description(self, place: Place):
        how_to_get_there = self.create_p_tag('How to get there', place.how_to_get_there)
        return f'{how_to_get_there}'

    def check_children(self, children):
        checked_children = []
        for child in children:
            if child is not None:
                checked_children.append(child)
        return checked_children

    def create_child(self, id: int, title: str, description: str):
        if not description.strip():
            return None
        return {
            'id': id,
            'title': title,
            'description': description
        }

    def get_sections(self, obj: Place):
        return [
            create_section_simple(
                  title='Info',
                  key='Info',
                  icon_name=IconNames.article,
                  display_type='drop_down',
                  children=self.check_children(
                    [
                        self.create_child(id=1,
                                          title='General info',
                                          description=self.general_info_description(obj)
                                          ),
                        self.create_child(id=2,
                                          title='Civilization',
                                          description=self.civilization_description(obj)
                                          ),
                    ]
                )
            ),
            create_section_nested(
                key="transports",
                obj=obj,
                icon_name=IconNames.directions,
                display_type="drop_down",
                create_children=self.transport_children,
            ),
            create_section_nested(
                key="must_sees",
                obj=obj,
                icon_name=IconNames.article,
                display_type="drop_down",
                create_children=self.must_see_children,
            ),
            create_section_nested(
                key="accommodation_options",
                obj=obj,
                icon_name=IconNames.bed,
                display_type="drop_down",
                create_children=self.accommodation_option_children,
            ),
            create_section_nested(
                key="flora_faunas",
                obj=obj,
                icon_name=IconNames.article,
                display_type="grid",
                create_children=self.flora_fauna_children,
            ),
            create_section_simple(
                title='Climate and geography',
                key='Climate and geography',
                icon_name=IconNames.article,
                display_type='drop_down',
                children=self.check_children(
                    [
                        self.create_child(id=1,
                                          title='Climatic condition',
                                          description=self.climatic_condition_description(obj),
                                          ),
                        self.create_child(id=2,
                                          title='Geographical feature',
                                          description=self.geographical_feature_description(obj)
                                          ),
                    ]
                ),
            ),
            create_section_simple(
                title='Additional info',
                key='Additional info',
                icon_name=IconNames.article,
                display_type='drop_down',
                children=self.check_children(
                    [
                        self.create_child(id=1,
                                          title='Nearest Airport',
                                          description=self.nearest_airport_description(obj),
                                          ),
                        self.create_child(id=2,
                                          title='How to get there',
                                          description=self.how_to_get_there_description(obj)),
                    ]
                )
            ),
        ]

'''
{
    "title": '',
    "key": '',
    "icon_name": IconNames.,
    "display_type": '',
    "children": [
        {
            'id': 1,
            'title': '',
            'description': "",
        },
        {
            'id': 2,
            'title': '',
            'description': "",
        },
    ],
},
'''

import mptt
from colorfield.fields import ColorField
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
# from django.contrib.gis.geos import Point
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
# from django.contrib.gis.db import models as geomodels
# from django_countries.fields import CountryField
# from location_field.forms.spatial import LocationField
# from location_field.models.plain import PlainLocationField
# from geopy import Point
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.translation import gettext_lazy as _


# Create your models here.

CONTINENT_CHOICES =(
    ("asia", "Asia"),
    ("africa", "Africa"),
    ("europe", "Europe"),
    ("north america", "North America"),
    ("south america", "South America"),
    ("australia/oceania", "Australia/Oceania"),
    ("antarctica", "Antarctica"),
)

TYPE_OF_PEOPLE_AROUND_CHOICES =(
    ("ambitious and passionate people", "Ambitious and passionate people"),
    ("the doers", "The doers"),
    ("the problem solvers", "The problem solvers"),
    ("those who are on a similar journey as you", "Those who are on a similar journey as you"),
    ("those who can inspire you and be your role model", "Those who can inspire you and be your role model"),
    ("those who help you tap your full potential and bring out the best in you", "Those who help you tap your full potential and bring out the best in you"),
    ("those who can provide a genuine feedback", "Those who can provide a genuine feedback"),
    ("those who can help you keep happy, upbeat and positive", "Those who can help you keep happy, upbeat and positive"),
    ("the ‘forward moving’ people", "The ‘forward moving’ people"),
)

HOW_DANGEROUS_CHOICES =(
    ("very safe", "Very Safe"),
    ("safe", "Safe"),
    ("average", "Average"),
    ("somewhat dangerous", "Somewhat Dangerous"),
    ("dangerous", "Dangerous"),

)

CLIMATE_CHOICES = (
    ("Tropical", "Tropical"),
    ("Dry", "Dry"),
    ("Mild", "Mild"),
    ("Continental", "Continental"),
    ("Polar", "Polar"),
)

HOW_COMFORTABLE_CHOICES = (
    ("Very Comfortable", "Very Comfortable"),
    ("Comfortable", "Comfortable"),
    ("Average", "Average"),
    ("Durable", "Durable"),
    ("Totally Uncomfortable", "Totally Uncomfortable"),

)

TYPES_OF_ECOSYSTEMS_CHOICES =(
    ("terrestrial ecosystem", "Terrestrial ecosystem"),
    ("forest ecosystem", "Forest ecosystem"),
    ("grassland ecosystem", "Grassland ecosystem"),
    ("desert ecosystem", "Desert ecosystem"),
    ("tundra ecosystem", "Tundra ecosystem"),
    ("freshwater ecosystem", "Freshwater ecosystem"),
    ("marine ecosystem", "Marine ecosystem"),
)

TYPES_OF_TRANSPORT_CHOICES = (
    ("Walking", "Walking"),
    ("Biking", "Biking"),
    ("Cars", "Cars"),
    ("Trains", "Trains"),
    ("Buses", "Buses"),
    ("Boats", "Boats"),
    ("Subways", "Subways"),
    ("Aerial Tramways", "Aerial Tramways"),
    ("Flying", "Flying"),
    ("Funiculars", "Funiculars"),
)

# class Category(MPTTModel):
#     class Meta:
#         db_table = 'category'
#         verbose_name_plural = "Category"
#         verbose_name = "Category"
#         ordering = ('tree_id', 'level')
#     name = models.CharField(max_length=255, verbose_name="Category", unique=True)
#     parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children', verbose_name="Parent class")
#
#     def __unicode__(self):
#         return self.name
#
#     class MPTTMeta:
#         order_insertion_by = ['name']
#
#     def __str__(self):
#         return f'{self.name}'
#
# mptt.register(Category, order_insertion_by=['name'])


class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), blank=False, unique=True)

    username = models.CharField(
        _("username"),
        max_length=150,
        help_text=_("Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.")
    )

    email_verify = models.BooleanField(default=False)

    # bookmark_place = models.ManyToManyField("Place", verbose_name="bookmark_places", related_name="bookmark_places",
    #                                         blank=True,)

    is_active = models.BooleanField(default=False)

    image = models.ImageField(upload_to='images/custom_user/', null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['is_active', 'username']

    def __str__(self):
        return self.email


# class TypeOfPeople(models.Model):
#     type = models.CharField(max_length=255)
#
#     def __str__(self):
#         return f'{self.type}'

class ClimaticCondition(models.Model):
    condition = models.CharField(max_length=255)
    climate = models.CharField(choices=CLIMATE_CHOICES, max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.condition} - {self.climate}'


class GeographicalFeature(models.Model):
    types_of_ecosystem = models.CharField(max_length=255, blank=True)
    types_of_ecosystem_description = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.types_of_ecosystem} - {self.types_of_ecosystem_description}'


class Category(MPTTModel):
    name = models.CharField(max_length=255, blank=False, unique=True)
    description = models.TextField(blank=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    color = ColorField(default='#FF0000')
    image = models.ImageField(upload_to='images/categories/', null=True, blank=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return f'{self.name}'

mptt.register(Category, order_insertion_by=['name'])

ICON_CHOICES = (
    ("article", "article"),
    ("bed", "bed"),
    ("people", "people"),
    ("cloud", "cloud"),
    ("restaurant_menu", "restaurant_menu"),
    ("attractions_rounded", "attractions_rounded"),
    ("grass", "grass"),
    ("done", "done"),
    ("star", "star"),
    ("lock", "lock"),
    ("terrain", "terrain"),
    ("directions", "directions"),
    ("camera", "camera"),
    ("surfing", "surfing"),
)

FIELD_TYPE_CHOICES = (
    ("charfield", "charfield"),
    ("textfield", "textfield"),
    ("intfield", "intfield"),
    ("floatfield", "floatfield"),
    ("imagefield", "imagefield"),
    ("multiselect", "multiselect"),
    ("picker", "picker"),
    ("multiimagefield", "multiimagefield"),
)


# class AttributesFamily(models.Model):
#     name = models.CharField(max_length=255)
#     icon = models.CharField(max_length=255, choices=ICON_CHOICES)
#
#
# class Attribute(models.Model):
#     name = models.CharField(max_length=255)
#     type = models.CharField(max_length=255, choices=FIELD_TYPE_CHOICES)
#     family = models.ForeignKey(Family, on_delete=models.CASCADE)

# To get input type of model field -> str
# Place._meta.get_field('name').get_internal_type()


class Place(models.Model):
    # families = models.ManyToManyField(AttributesFamily)
    is_active = models.BooleanField(default=False)
    writer_user = models.ForeignKey(CustomUser, verbose_name='writer_user', related_name="writer_user", on_delete=models.CASCADE)
    # bookmark_place = models.ManyToManyField(CustomUser, verbose_name="bookmark_customuser", related_name="bookmark_customuser",
    #                                         blank=True,)
    home_page = models.BooleanField(default=False)
    name = models.CharField(max_length=255, blank=False, default=f"Place name")
    nickname = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    categories = models.ManyToManyField(Category, blank=True)
    climatic_condition = models.ForeignKey(ClimaticCondition, on_delete=models.CASCADE, null=True, blank=True)
    geographical_feature = models.ForeignKey(GeographicalFeature, on_delete=models.CASCADE, null=True, blank=True)
    nearest_airport = models.TextField(null=True, blank=True)
    how_to_get_there = models.TextField(null=True, blank=True)
    population = models.BigIntegerField(null=True, blank=True)
    # type_of_people_around = models.ForeignKey(TypeOfPeople, on_delete=models.CASCADE, blank=True, null=True,
    #                                           related_name="civilizations")
    type_of_people_around = models.TextField(null=True, blank=True)
    nation = models.TextField(null=True, blank=True)
    language = models.CharField(max_length=255, null=True, blank=True)
    culture = models.TextField(null=True, blank=True)
    turist_rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)],
                                        blank=False, null=True, default=None)
    # turist_description = models.TextField(blank=True, null=True)
    # tourist_population_per_season_winter = models.BigIntegerField(null=True, blank=True)
    # tourist_population_per_season_spring = models.BigIntegerField(null=True, blank=True)
    # tourist_population_per_season_summer = models.BigIntegerField(null=True, blank=True)
    # tourist_population_per_season_autumn = models.BigIntegerField(null=True, blank=True)
    currency = models.CharField(max_length=255, null=True, blank=True)
    currency_buying_advice = models.TextField(null=True, blank=True)
    simcards = models.TextField(null=True, blank=True)
    internet = models.TextField(null=True, blank=True)
    pay_online_or_by_card = models.CharField(max_length=255, null=True, blank=True)
    views = models.ManyToManyField(CustomUser, through="UserPlaceRelation", blank=True)
    # geolocation = geomodels.PointField("Location in Map", geography=True, blank=True, null=True,
    #     srid=4326, help_text="Point(longitude latitude)")
    # location = PlainLocationField(based_fields=['city'], zoom=7, default=Point(1.0, 1.0))
    # coordinate = geomodels.PointField(geography=True, spatial_index=True,default=Point(58.238056, 37.862499, srid=4326), blank=True, null=True)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)],
                                 null=True, blank=False, default=None)

    # category = TreeForeignKey(Category, verbose_name="categorys", related_name="categorys", on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return f'{self.id}: {self.name}'
# ----------------------------------------------------------------------------------------


class UserPlaceRelation(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name="user_place")
    in_bookmarks = models.BooleanField(default=False)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], blank=False)
    rating_description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} {self.place.name}, {self.rating}"


# class WorldBorder(geomodels.Model):
#     # Regular Django fields corresponding to the attributes in the
#     # world borders shapefile.
#     name = models.CharField(max_length=50)
#     area = models.IntegerField()
#     pop2005 = models.IntegerField('Population 2005')
#     fips = models.CharField('FIPS Code', max_length=2, null=True)
#     iso2 = models.CharField('2 Digit ISO', max_length=2)
#     iso3 = models.CharField('3 Digit ISO', max_length=3)
#     un = models.IntegerField('United Nations Code')
#     region = models.IntegerField('Region Code')
#     subregion = models.IntegerField('Sub-Region Code')
#     lon = models.FloatField()
#     lat = models.FloatField()
#
#     # GeoDjango-specific: a geometry field (MultiPolygonField)
#     mpoly = geomodels.MultiPolygonField()
#
#     # Returns the string representation of the model.
#     def __str__(self):
#         return self.name

# Auto-generated `LayerMapping` dictionary for WorldBorder model
# worldborder_mapping = {
#     'fips': 'FIPS',
#     'iso2': 'ISO2',
#     'iso3': 'ISO3',
#     'un': 'UN',
#     'name': 'NAME',
#     'area': 'AREA',
#     'pop2005': 'POP2005',
#     'region': 'REGION',
#     'subregion': 'SUBREGION',
#     'lon': 'LON',
#     'lat': 'LAT',
#     'geom': 'MULTIPOLYGON',
# }


class Location(models.Model):
    place = models.ForeignKey(Place, related_name="locations", on_delete=models.CASCADE)
    continent = models.CharField(choices=CONTINENT_CHOICES, max_length=20, default="Asia")
    country = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    county = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    latitude = models.DecimalField(max_digits=13, decimal_places=10, null=True, blank=True)
    longitude = models.DecimalField(max_digits=13, decimal_places=10, null=True, blank=True)
    nearest_place = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.continent} {self.country} {self.state} {self.city} {self.latitude} {self.longitude} {self.nearest_place}"


# class Location(MPTTModel):
#     place = models.ForeignKey(Place, related_name="locations", on_delete=models.CASCADE)
#     name = models.CharField(max_length=50, unique=True)
#     parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
#
#     def __unicode__(self):
#         return self.name
#
#     class MPTTMeta:
#         order_insertion_by = ['name']
#
#     def __str__(self):
#         return f'{self.name}'
#
# mptt.register(Location, order_insertion_by=['name'])


class TypeTransport(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'


class Transport(models.Model):
    place = models.ForeignKey(Place, related_name="transports", on_delete=models.CASCADE)
    type_transport = models.ForeignKey(TypeTransport, related_name="transports", on_delete=models.CASCADE, blank=False)
    price = models.DecimalField(max_digits=13, decimal_places=2, default=None, blank=False)
    description = models.TextField(null=True, blank=True)
    comfortable = models.CharField(choices=HOW_COMFORTABLE_CHOICES, max_length=255)
    image = models.ImageField(upload_to='images/transports/', null=True, blank=True)

    def __str__(self):
        return f"{self.type_transport} {self.price} {self.description} {self.comfortable} {self.image}"


class Safe(models.Model):
    name = models.CharField(max_length=255, blank=False, default=None)
    place = models.ForeignKey(Place, related_name="safes", on_delete=models.CASCADE)
    how_dangerous = models.CharField(choices=HOW_DANGEROUS_CHOICES, max_length=255, blank=True)
    rating_danger = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], blank=False)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.how_dangerous} {self.rating_danger} {self.description}"


class TypeCuisine(models.Model):
    type = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.type}'


class Cuisine(models.Model):
    place = models.ForeignKey(Place, related_name="cuisines", on_delete=models.CASCADE)
    name = models.ForeignKey(TypeCuisine, on_delete=models.CASCADE, blank=False, related_name="cuisines")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=None, blank=False)
    # type_cuisine = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/cuisines/', null=True, blank=True)

    def __str__(self):
        return f"{self.place.name} {self.name}"


class Entertainment(models.Model):
    place = models.ForeignKey(Place, related_name="entertainments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=False, default=None)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images/entertainments/', null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.description} {self.image}"


class NaturalPhenomena(models.Model):
    place = models.ForeignKey(Place, related_name="natural_phenomenas", on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=False, default=None)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images/natural_phenomenas/', null=True, blank=True)

    def __str__(self):
        return f"{self.name}  {self.description} {self.image}"


class Image(models.Model):
    place = models.ForeignKey(Place, related_name="images", blank=True, null=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/places/', blank=False, null=True)

    def __str__(self):
        return f"{self.path}"


class AccommodationOption(models.Model):
    name = models.CharField(max_length=255, blank=False, default=None)
    place = models.ForeignKey(Place, related_name="accommodation_options", on_delete=models.CASCADE, null=True)
    price = models.DecimalField(max_digits=13, decimal_places=2, blank=False, default=10)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.price} {self.description}"


class UniquenessPlace(models.Model):
    name = models.CharField(max_length=255, blank=False, default=None)
    place = models.ForeignKey(Place, related_name="uniqueness_places", on_delete=models.CASCADE, null=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/uniqueness_places/', null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.description} {self.image}"


class MustSee(models.Model):
    name = models.CharField(max_length=255, blank=False, default=None)
    place = models.ForeignKey(Place, related_name="must_sees", on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/must_sees/', null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.description} {self.image}"


class Vibe(models.Model):
    place = models.ForeignKey(Place, related_name="vibes", on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=False, default=None)
    image = models.ImageField(upload_to='images/vibes/', null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.image}"


class WhereToTakeAPicture(models.Model):
    name = models.CharField(max_length=255, blank=False, default=None)
    place = models.ForeignKey(Place, related_name="where_to_take_a_pictures", on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/where_to_take_a_pictures/', null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.description} {self.image}"


class InterestingFacts(models.Model):
    place = models.ForeignKey(Place, related_name="interesting_facts", on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/interesting_facts/', null=True, blank=True)

    def __str__(self):
        return f"{self.place.name} {self.description}"


class PracticalInformation(models.Model):
    place = models.ForeignKey(Place, related_name="practical_informations", on_delete=models.CASCADE)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.place.name} {self.description}"


class FloraFauna(models.Model):
    place = models.ForeignKey(Place, related_name="flora_faunas", on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=False, default=None)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/flora_faunas/', blank=False, default=None)

    def __str__(self):
        return f"{self.place.name} {self.name}"


class Bookmark(models.Model):
    place = models.ForeignKey(Place, related_name="bookmarks", on_delete=models.CASCADE, blank=False)
    user = models.ForeignKey(CustomUser, related_name="bookmarks", on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return f"{self.user.username} - {self.place.name}"


class Group(models.Model):
    name = models.CharField(max_length=255)
    places = models.ManyToManyField(Place, blank=True)

    def __str__(self):
        return f'{self.name}'

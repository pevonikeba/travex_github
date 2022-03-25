import mptt
from colorfield.fields import ColorField
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django_countries.fields import CountryField
from mptt.models import MPTTModel, TreeForeignKey

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

CLIMATE_CHOICES =(
    ("Tropical", "Tropical"),
    ("Dry", "Dry"),
    ("Mild", "Mild"),
    ("Continental", "Continental"),
    ("Polar", "Polar"),
)

HOW_COMFORTABLE_CHOICES = (
    ("very comfortable", "Very Comfortable"),
    ("comfortable", "Comfortable"),
    ("average", "Average"),
    ("durable", "Durable"),
    ("totally uncomfortable", "Totally Uncomfortable"),

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

TYPES_OF_TRANSPORT_CHOICES =(
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


class TypeOfPeople(models.Model):
    type = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.type}'

class ClimaticConditions(models.Model):
    conditions = models.CharField(max_length=255)
    climate = models.CharField(choices=CLIMATE_CHOICES, max_length=255)

    def __str__(self):
        return f'{self.conditions} - {self.climate}'

class TypeOfTerrain(models.Model):
    types_of_ecosystem = models.CharField(max_length=255, blank=True)
    types_of_ecosystem_description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.types_of_ecosystem} - {self.types_of_ecosystem_description}'

class Category(MPTTModel):
    name = models.CharField(max_length=255, blank=True, unique=True)
    description = models.TextField(blank=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    color = ColorField(default='#FF0000')
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return f'{self.name}'

mptt.register(Category, order_insertion_by=['name'])

class Place(models.Model):

    writer_user = models.ForeignKey(User, verbose_name='writer_user', related_name="writer_user", on_delete=models.CASCADE)

    home_page = models.BooleanField(default=False)

    name = models.CharField(max_length=255, blank=False, default=None)
    nickname = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True)

    category = models.ManyToManyField(Category, verbose_name="categories", related_name="categories",
                                      blank=True)

    climate = models.ForeignKey(ClimaticConditions, on_delete=models.CASCADE, null=True, blank=True)
    climate_description = models.TextField(null=True, blank=True)

    type_of_terrain = models.ForeignKey(TypeOfTerrain, on_delete=models.CASCADE, null=True, blank=True)
    type_of_terrain_description = models.TextField(null=True, blank=True)

    nearest_airport = models.TextField(null=True, blank=True)

    how_to_get_there = models.TextField(null=True, blank=True)

    population = models.BigIntegerField(null=True, blank=True)
    type_of_people_around = models.ForeignKey(TypeOfPeople, on_delete=models.CASCADE, blank=True, null=True,
                                              related_name="civilizations")
    nation = models.TextField(blank=True, null=True)
    language = models.CharField(blank=True, null=True, max_length=255)
    culture = models.TextField(blank=True, null=True)

    turist_description = models.TextField(blank=True, null=True)
    tourist_population_per_season_winter = models.BigIntegerField(null=True, blank=True)
    tourist_population_per_season_spring = models.BigIntegerField(null=True, blank=True)
    tourist_population_per_season_summer = models.BigIntegerField(null=True, blank=True)
    tourist_population_per_season_autumn = models.BigIntegerField(null=True, blank=True)


    currency = models.TextField(null=True, blank=True)
    currency_buying_advice = models.TextField(null=True, blank=True)
    simcards = models.TextField(blank=True, null=True)
    internet = models.TextField(null=True, blank=True)
    pay_online_or_by_card = models.TextField(null=True, blank=True)

    views = models.ManyToManyField(User, through="UserPlaceRelation", related_name="views")

    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], blank=False, default=None)

    # category = TreeForeignKey(Category, verbose_name="categorys", related_name="categorys", on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return f'{self.id}: {self.name}'

#---------------------------------------------------------------------------------------------------------------------------------------------------------



class UserPlaceRelation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name="user_place")
    in_bookmarks = models.BooleanField(default=False)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], blank=False)
    description_rating = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} {self.place.name}, {self.rating}"

class Location(models.Model):
    place = models.ForeignKey(Place, related_name="locations", on_delete=models.CASCADE)
    continent = models.CharField(choices=CONTINENT_CHOICES, max_length=20, default="Asia")
    country = CountryField(null=True, blank=True)
    region = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    latitude = models.DecimalField(max_digits=13, decimal_places=10, null=True, blank=True)
    longitude = models.DecimalField(max_digits=13, decimal_places=10, null=True, blank=True)
    nearest_place = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.continent} {self.country} {self.region} {self.city} {self.latitude} {self.longitude} {self.nearest_place}"


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

class Transport(models.Model):
    place = models.ForeignKey(Place, related_name="transports", on_delete=models.CASCADE)
    name = models.CharField(choices=TYPES_OF_TRANSPORT_CHOICES, blank=False, default=None, max_length=255)
    price = models.DecimalField(max_digits=13, decimal_places=2, default=10, blank=False)
    description = models.TextField(null=True, blank=True)
    comfortable = models.CharField(choices=HOW_COMFORTABLE_CHOICES, max_length=255)
    image = models.ImageField(upload_to='images/', null=True, blank=True)


    def __str__(self):
        return f"{self.name} {self.price} {self.description} {self.comfortable} {self.image}"


class Safe(models.Model):
    name = models.CharField(max_length=255, blank=False, default=None)
    place = models.ForeignKey(Place, related_name="safes", on_delete=models.CASCADE)
    how_dangerous = models.CharField(choices=HOW_DANGEROUS_CHOICES, max_length=255, blank=True)
    rating_danger = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], blank=False)
    description = models.TextField(blank=True, null=True)
    def __str__(self):
        return f"{self.how_dangerous} {self.rating_danger} {self.description}"


class Cuisine(models.Model):
    place = models.ForeignKey(Place, related_name="cuisines", on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=False, default=None)
    type_cuisine = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=10, blank=False)

    def __str__(self):
        return f"{self.place.name} {self.name}"

class Entertainment(models.Model):
    place = models.ForeignKey(Place, related_name="entertainments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=False, default=None)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.description} {self.image}"


class NaturalPhenomena(models.Model):
    place = models.ForeignKey(Place, related_name="natural_phenomena", on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=False, default=None)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return f"{self.name}  {self.description} {self.image}"



class Image(models.Model):
    path = models.ImageField(upload_to='images/', blank=False, default=None)
    place = models.ForeignKey(Place, related_name="images", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.path}"


class AccommodationOptions(models.Model):
    name = models.CharField(max_length=255, blank=False, default=None)
    place = models.ForeignKey(Place, related_name="accommodationOptions", on_delete=models.CASCADE, null=True)
    price = models.DecimalField(max_digits=13, decimal_places=2, blank=False, default=10)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.price} {self.description}"


class UniquenessPlace(models.Model):
    name = models.CharField(max_length=255, blank=False, default=None)
    place = models.ForeignKey(Place, related_name="uniqueness_place", on_delete=models.CASCADE, null=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.description} {self.image}"

class MustSee(models.Model):
    name = models.CharField(max_length=255, blank=False, default=None)
    place = models.ForeignKey(Place, related_name="must_see", on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.description} {self.image}"

class Vibe(models.Model):
    place = models.ForeignKey(Place, related_name="vibes", on_delete=models.CASCADE)
    vibe = models.CharField(max_length=255, blank=False, default=None)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return f"{self.vibe} {self.image}"

class WhereToTakeAPicture(models.Model):
    name = models.CharField(max_length=255, blank=False, default=None)
    place = models.ForeignKey(Place, related_name="where_to_take_a_picture", on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.description} {self.image}"

class InterestingFacts(models.Model):
    place = models.ForeignKey(Place, related_name="interesting_facts", on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return f"{self.place.name} {self.description}"

class FloraAndFauna(models.Model):
    place = models.ForeignKey(Place, related_name="flora_fauna", on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=False, default=None)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/', blank=False, default=None)

    def __str__(self):
        return f"{self.place.name} {self.name}"



class Group(models.Model):
    name = models.CharField(max_length=255)
    places = models.ManyToManyField(Place, verbose_name="places", related_name="places",
                                    blank=True, )

    def __str__(self):
        return f'{self.name}'
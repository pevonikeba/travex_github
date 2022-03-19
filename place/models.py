from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django_countries.fields import CountryField
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


class ImageField(models.ImageField):
    def value_to_string(self, obj): # obj is Model instance, in this case, obj is 'Class'
        return obj.fig.url # not return self.url

class Place(models.Model):
    name = models.CharField(max_length=255)
    nickname = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True)
    nearest_place = models.TextField(null=True, blank=True)

    population = models.BigIntegerField(null=True, blank=True)
    type_of_people_around = models.CharField(choices=TYPE_OF_PEOPLE_AROUND_CHOICES, max_length=255, blank=True)

    how_dangerous = models.CharField(choices=HOW_DANGEROUS_CHOICES, max_length=255, blank=True)
    rating_danger = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)], default=5.0)

    types_of_ecosystem = models.CharField(choices=TYPES_OF_ECOSYSTEMS_CHOICES, max_length=255, blank=True)
    types_of_ecosystem_description = models.TextField(null=True, blank=True)

    tourist_population_per_season_winter = models.BigIntegerField(null=True, blank=True)
    tourist_population_per_season_spring = models.BigIntegerField(null=True, blank=True)
    tourist_population_per_season_summer = models.BigIntegerField(null=True, blank=True)
    tourist_population_per_season_autumn = models.BigIntegerField(null=True, blank=True)

    transport = models.TextField(null=True, blank=True)
    nearest_airport = models.TextField(null=True, blank=True)

    kitchen = models.TextField(null=True, blank=True)
    local_kitchen = models.TextField(null=True, blank=True)
    price_and_average_kitchen = models.TextField(null=True, blank=True)

    currency = models.TextField(null=True, blank=True)
    currency_buying_advice = models.TextField(null=True, blank=True)
    simcards = models.TextField(null=True, blank=True)
    internet = models.TextField(null=True, blank=True)
    pay_online_or_by_card = models.TextField(null=True, blank=True)

    rating = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)], default=5.0)

    def __str__(self):
        return f'{self.id}:  {self.name}'


class Location(models.Model):
    place = models.ForeignKey(Place, related_name="locations", on_delete=models.CASCADE)
    continent = models.CharField(choices=CONTINENT_CHOICES, max_length=20, default="Asia")
    country = CountryField()
    region = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    latitude = models.DecimalField(max_digits=13, decimal_places=10, null=True, blank=True)
    longitude = models.DecimalField(max_digits=13, decimal_places=10, null=True, blank=True)

    def __str__(self):
        return f'{self.id}: {self.country} - {self.region} - {self.city}'

class Climate(models.Model):
    climate = models.CharField(choices=CLIMATE_CHOICES, max_length=255, blank=True)
    climate_description = models.TextField(null=True, blank=True)
    tips_for_every_season = models.TextField(null=True, blank=True)


class Transport(models.Model):
    place = models.ForeignKey(Place, related_name="transports", on_delete=models.CASCADE)
    name = models.CharField(choices=TYPES_OF_TRANSPORT_CHOICES, null=True, max_length=255)
    price = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    comfortable = models.CharField(choices=HOW_COMFORTABLE_CHOICES, max_length=255)
    image = models.ImageField(upload_to='images/', null=True, blank=True)


    def __str__(self):
        return f'{self.id}: {self.name} - {self.price}$'



class Image(models.Model):
    path = ImageField(upload_to='images/', null=True, blank=True)
    place = models.ForeignKey(Place, related_name="images", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.path}'


class AccommodationOptions(models.Model):
    name = models.CharField(max_length=255, null=True)
    place = models.ForeignKey(Place, related_name="accommodationOptions", on_delete=models.CASCADE, null=True)
    price = models.DecimalField(max_digits=13, decimal_places=2, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.id}: {self.name} - {self.price}$'


class UniquenessPlace(models.Model):
    name = models.CharField(max_length=255)
    place = models.ForeignKey(Place, related_name="uniqueness_place", on_delete=models.CASCADE, null=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return f'{self.id}: {self.name} - {self.description}'

class MustSee(models.Model):
    name = models.CharField(max_length=255)
    place = models.ForeignKey(Place, related_name="must_see", on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return f'{self.id}: {self.name} - {self.description}'

class WhereToTakeAPicture(models.Model):
    name = models.CharField(max_length=255)
    place = models.ForeignKey(Place, related_name="where_to_take_a_picture", on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return f'{self.id}: {self.name} - {self.description}'




class Group(models.Model):
    name = models.CharField(max_length=255)
    places = models.ManyToManyField(Place, verbose_name="places", related_name="places",
                                    blank=True, )
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return  f'{self.id}: {self.name}'
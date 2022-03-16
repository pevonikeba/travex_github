from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.



class Place(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=13, decimal_places=10, null=True, blank=True)
    longitude = models.DecimalField(max_digits=13, decimal_places=10, null=True, blank=True)
    rating = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)], default=5.0)

    def __str__(self):
        return f'{self.id}: {self.name}'


class Image(models.Model):
    path = models.ImageField(upload_to='images/', null=True, blank=True)
    place = models.ForeignKey(Place, related_name="images", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.path}'


class Group(models.Model):
    name = models.CharField(max_length=255)
    places = models.ManyToManyField(Place, verbose_name="places", related_name="places",
                                    blank=True, )
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return  f'{self.id}: {self.name}'
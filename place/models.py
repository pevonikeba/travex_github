from django.db import models

# Create your models here.


class Place(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    # images = models.ImageField(upload_to='images')

    def __str__(self):
        return f'{self.id}: {self.name}'


class Groups(models.Model):
    name = models.CharField(max_length=255)
    places = models.ManyToManyField(Place, verbose_name="places",
                                    blank=True, )

    def __str__(self):
        return  f'{self.id}: {self.name}'
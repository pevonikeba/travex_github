# Generated by Django 4.0.3 on 2022-03-17 11:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0023_place_type_of_people_around_alter_place_city_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='climate',
            field=models.CharField(blank=True, choices=[('Tropical', 'Tropical'), ('Dry', 'Dry'), ('Mild', 'Mild'), ('Continental', 'Continental'), ('Polar', 'Polar')], max_length=255),
        ),
        migrations.AddField(
            model_name='place',
            name='climate_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='place',
            name='how_dangerous',
            field=models.CharField(blank=True, choices=[('small', 'Small'), ('medium', 'Medium'), ('hard', 'Hard')], max_length=255),
        ),
        migrations.AddField(
            model_name='place',
            name='rating_danger',
            field=models.FloatField(default=5.0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(5.0)]),
        ),
        migrations.AddField(
            model_name='place',
            name='tips_for_every_season',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='place',
            name='types_of_ecosystem',
            field=models.CharField(blank=True, choices=[('terrestrial ecosystem', 'Terrestrial ecosystem'), ('forest ecosystem', 'Forest ecosystem'), ('grassland ecosystem', 'Grassland ecosystem'), ('desert ecosystem', 'Desert ecosystem'), ('tundra ecosystem', 'Tundra ecosystem'), ('freshwater ecosystem', 'Freshwater ecosystem'), ('marine ecosystem', 'Marine ecosystem')], max_length=255),
        ),
        migrations.AddField(
            model_name='place',
            name='types_of_ecosystem_description',
            field=models.TextField(blank=True, null=True),
        ),
    ]

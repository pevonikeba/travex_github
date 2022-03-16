# Generated by Django 4.0.3 on 2022-03-16 11:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0005_place_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='rating',
        ),
        migrations.AddField(
            model_name='place',
            name='rate',
            field=models.FloatField(default=5.0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(5.0)]),
        ),
    ]

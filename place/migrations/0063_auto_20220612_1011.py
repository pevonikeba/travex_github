# Generated by Django 3.2.13 on 2022-06-12 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0062_remove_place_location2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=13, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=13, null=True),
        ),
    ]
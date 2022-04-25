# Generated by Django 3.2.13 on 2022-04-25 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0011_alter_group_place'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='place',
        ),
        migrations.AddField(
            model_name='group',
            name='places',
            field=models.ManyToManyField(blank=True, related_name='places', to='place.Place', verbose_name='place'),
        ),
    ]

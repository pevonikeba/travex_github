# Generated by Django 3.2.13 on 2022-04-25 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0010_auto_20220425_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='place',
            field=models.ManyToManyField(blank=True, to='place.Place'),
        ),
    ]
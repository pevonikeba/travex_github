# Generated by Django 3.2.13 on 2022-04-29 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0017_auto_20220426_0759'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Image',
            new_name='PlaceImage',
        ),
    ]

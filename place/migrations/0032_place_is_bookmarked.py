# Generated by Django 3.2.13 on 2022-05-11 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0031_auto_20220510_1251'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='is_bookmarked',
            field=models.BooleanField(default=False),
        ),
    ]

# Generated by Django 3.2.13 on 2022-05-05 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0022_auto_20220504_1243'),
    ]

    operations = [
        migrations.AddField(
            model_name='transport',
            name='description_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='transport',
            name='description_ru',
            field=models.TextField(blank=True, null=True),
        ),
    ]

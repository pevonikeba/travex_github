# Generated by Django 3.2.13 on 2022-05-05 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0023_auto_20220505_0716'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transport',
            name='description_en',
        ),
        migrations.RemoveField(
            model_name='transport',
            name='description_ru',
        ),
    ]
# Generated by Django 4.0.3 on 2022-04-16 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='region',
            new_name='state',
        ),
    ]
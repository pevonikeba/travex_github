# Generated by Django 4.0.3 on 2022-04-15 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0036_alter_accommodationoptions_place_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]

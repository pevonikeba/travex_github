# Generated by Django 3.2.13 on 2022-05-17 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0038_rename_bookmarks_place_bookmarked_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='florafauna',
            name='image',
            field=models.ImageField(default='', upload_to='images/flora_faunas/'),
            preserve_default=False,
        ),
    ]
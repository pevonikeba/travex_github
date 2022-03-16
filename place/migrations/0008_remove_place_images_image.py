# Generated by Django 4.0.3 on 2022-03-16 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0007_rename_rate_place_rating_place_latitude_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='images',
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='place.place')),
            ],
        ),
    ]

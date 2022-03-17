# Generated by Django 4.0.3 on 2022-03-17 06:09

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0019_alter_place_city_alter_place_region'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('continent', models.CharField(choices=[('asia', 'Asia'), ('africa', 'Africa'), ('europe', 'Europe'), ('north america', 'North America'), ('south america', 'South America'), ('australia/oceania', 'Australia/Oceania'), ('antarctica', 'Antarctica')], default='Asia', max_length=20)),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2)),
                ('region', models.CharField(max_length=255, null=True)),
                ('city', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='place',
            name='city',
        ),
        migrations.RemoveField(
            model_name='place',
            name='continent',
        ),
        migrations.RemoveField(
            model_name='place',
            name='country',
        ),
        migrations.RemoveField(
            model_name='place',
            name='region',
        ),
        migrations.AddField(
            model_name='place',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='place.location'),
        ),
    ]

# Generated by Django 4.0.3 on 2022-03-19 23:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClimaticConditions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conditions', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='place',
            name='nearest_place',
        ),
        migrations.AddField(
            model_name='location',
            name='nearest_place',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='place',
            name='climate',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='place.climaticconditions'),
        ),
    ]

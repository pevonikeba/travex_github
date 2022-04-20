# Generated by Django 3.2.13 on 2022-04-20 07:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0004_alter_place_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transport',
            name='name',
        ),
        migrations.AddField(
            model_name='transport',
            name='type_transport',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='transport', to='place.typetransport'),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.0.3 on 2022-03-20 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0011_typeofpeople_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='civilization',
            name='type_of_people_around',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='civilizations', to='place.typeofpeople'),
        ),
    ]

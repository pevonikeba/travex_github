# Generated by Django 3.2.13 on 2022-05-01 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0019_auto_20220501_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transport',
            name='comfortable',
            field=models.CharField(blank=True, choices=[('Very Comfortable', 'Very Comfortable'), ('Comfortable', 'Comfortable'), ('Average', 'Average'), ('Durable', 'Durable'), ('Totally Uncomfortable', 'Totally Uncomfortable')], max_length=255, null=True),
        ),
    ]

# Generated by Django 3.2.13 on 2022-07-02 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0066_userlocation'),
    ]

    operations = [
        migrations.AddField(
            model_name='userlocation',
            name='postal_code',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
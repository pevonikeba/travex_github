# Generated by Django 3.2.13 on 2022-07-20 06:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0070_auto_20220714_1053'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='city',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='country',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='country_code',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='county',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='district',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='house_number',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='iso_3166_2_lvl4',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='location_id',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='longitude',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='municipality',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='point',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='postal_code',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='region',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='road',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='state',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='subdistrict',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='subregion',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='town',
        ),
        migrations.RemoveField(
            model_name='place',
            name='city',
        ),
        migrations.RemoveField(
            model_name='place',
            name='country',
        ),
        migrations.RemoveField(
            model_name='place',
            name='country_code',
        ),
        migrations.RemoveField(
            model_name='place',
            name='county',
        ),
        migrations.RemoveField(
            model_name='place',
            name='district',
        ),
        migrations.RemoveField(
            model_name='place',
            name='house_number',
        ),
        migrations.RemoveField(
            model_name='place',
            name='iso_3166_2_lvl4',
        ),
        migrations.RemoveField(
            model_name='place',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='place',
            name='location_id',
        ),
        migrations.RemoveField(
            model_name='place',
            name='longitude',
        ),
        migrations.RemoveField(
            model_name='place',
            name='municipality',
        ),
        migrations.RemoveField(
            model_name='place',
            name='point',
        ),
        migrations.RemoveField(
            model_name='place',
            name='postal_code',
        ),
        migrations.RemoveField(
            model_name='place',
            name='region',
        ),
        migrations.RemoveField(
            model_name='place',
            name='road',
        ),
        migrations.RemoveField(
            model_name='place',
            name='state',
        ),
        migrations.RemoveField(
            model_name='place',
            name='subdistrict',
        ),
        migrations.RemoveField(
            model_name='place',
            name='subregion',
        ),
        migrations.RemoveField(
            model_name='place',
            name='town',
        ),
    ]
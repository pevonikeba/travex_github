# Generated by Django 3.2.13 on 2022-07-21 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0003_auto_20220712_1409'),
    ]

    operations = [
        migrations.AddField(
            model_name='userlocation',
            name='place_type',
            field=models.CharField(blank=True, choices=[('hm', 'Home'), ('wk', 'Work'), ('ot', 'Other')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='placelocation',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=23, null=True),
        ),
        migrations.AlterField(
            model_name='placelocation',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=23, null=True),
        ),
        migrations.AlterField(
            model_name='userlocation',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=23, null=True),
        ),
        migrations.AlterField(
            model_name='userlocation',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=23, null=True),
        ),
    ]
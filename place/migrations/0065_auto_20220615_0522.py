# Generated by Django 3.2.13 on 2022-06-15 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0064_delete_climaticconditiomm'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='age',
        ),
        migrations.AddField(
            model_name='customuser',
            name='birth',
            field=models.DateField(blank=True, null=True),
        ),
    ]
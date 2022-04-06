# Generated by Django 4.0.3 on 2022-04-05 14:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0017_customuser_bookmark_place_alter_customuser_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='bookmark_place',
        ),
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='place.place')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

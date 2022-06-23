# Generated by Django 3.2.13 on 2022-06-23 16:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notification', '0012_auto_20220623_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notificationsend',
            name='topic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='notification.topic'),
        ),
        migrations.AlterField(
            model_name='notificationsend',
            name='users',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]

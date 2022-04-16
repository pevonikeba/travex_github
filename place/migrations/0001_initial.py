# Generated by Django 4.0.3 on 2022-04-16 12:12

import colorfield.fields
from django.conf import settings
import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('username', models.CharField(help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, verbose_name='username')),
                ('email_verify', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True)),
                ('color', colorfield.fields.ColorField(default='#FF0000', image_field=None, max_length=18, samples=None)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='place.category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ClimaticConditions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conditions', models.CharField(max_length=255)),
                ('climate', models.CharField(choices=[('Tropical', 'Tropical'), ('Dry', 'Dry'), ('Mild', 'Mild'), ('Continental', 'Continental'), ('Polar', 'Polar')], max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='GeographicalFeature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('types_of_ecosystem', models.CharField(blank=True, max_length=255)),
                ('types_of_ecosystem_description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_page', models.BooleanField(default=False)),
                ('name', models.CharField(default=None, max_length=255)),
                ('nickname', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(null=True)),
                ('climate_description', models.TextField(blank=True, null=True)),
                ('geographical_feature_description', models.TextField(blank=True, null=True)),
                ('nearest_airport', models.TextField(blank=True, null=True)),
                ('how_to_get_there', models.TextField(blank=True, null=True)),
                ('population', models.BigIntegerField(blank=True, null=True)),
                ('type_of_people_around', models.TextField()),
                ('nation', models.TextField(blank=True, null=True)),
                ('language', models.CharField(blank=True, max_length=255, null=True)),
                ('culture', models.TextField(blank=True, null=True)),
                ('turist_rating', models.IntegerField(default=None, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('currency', models.TextField(blank=True, null=True)),
                ('currency_buying_advice', models.TextField(blank=True, null=True)),
                ('simcards', models.TextField(blank=True, null=True)),
                ('internet', models.TextField(blank=True, null=True)),
                ('pay_online_or_by_card', models.TextField(blank=True, null=True)),
                ('rating', models.IntegerField(default=None, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('category', models.ManyToManyField(blank=True, to='place.category')),
                ('climate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='place.climaticconditions')),
                ('geographical_feature', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='place.geographicalfeature')),
            ],
        ),
        migrations.CreateModel(
            name='TypeCuisine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TypeTransport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='WhereToTakeAPicture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='where_to_take_a_picture', to='place.place')),
            ],
        ),
        migrations.CreateModel(
            name='Vibe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vibe', to='place.place')),
            ],
        ),
        migrations.CreateModel(
            name='UserPlaceRelation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('in_bookmarks', models.BooleanField(default=False)),
                ('rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('description_rating', models.TextField(blank=True, null=True)),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_place', to='place.place')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UniquenessPlace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('place', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='uniqueness_place', to='place.place')),
            ],
        ),
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, default=None, max_digits=13)),
                ('description', models.TextField(blank=True, null=True)),
                ('comfortable', models.CharField(choices=[('very comfortable', 'Very Comfortable'), ('comfortable', 'Comfortable'), ('average', 'Average'), ('durable', 'Durable'), ('totally uncomfortable', 'Totally Uncomfortable')], max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='place.typetransport')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transport', to='place.place')),
            ],
        ),
        migrations.CreateModel(
            name='Safe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=255)),
                ('how_dangerous', models.CharField(blank=True, choices=[('very safe', 'Very Safe'), ('safe', 'Safe'), ('average', 'Average'), ('somewhat dangerous', 'Somewhat Dangerous'), ('dangerous', 'Dangerous')], max_length=255)),
                ('rating_danger', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('description', models.TextField(blank=True, null=True)),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='safe', to='place.place')),
            ],
        ),
        migrations.CreateModel(
            name='PracticalInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True)),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='practical_information', to='place.place')),
            ],
        ),
        migrations.AddField(
            model_name='place',
            name='views',
            field=models.ManyToManyField(related_name='views', through='place.UserPlaceRelation', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='place',
            name='writer_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='writer_user', to=settings.AUTH_USER_MODEL, verbose_name='writer_user'),
        ),
        migrations.CreateModel(
            name='NaturalPhenomena',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='natural_phenomena', to='place.place')),
            ],
        ),
        migrations.CreateModel(
            name='MustSee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='must_see', to='place.place')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('continent', models.CharField(choices=[('asia', 'Asia'), ('africa', 'Africa'), ('europe', 'Europe'), ('north america', 'North America'), ('south america', 'South America'), ('australia/oceania', 'Australia/Oceania'), ('antarctica', 'Antarctica')], default='Asia', max_length=20)),
                ('country', models.CharField(blank=True, max_length=255, null=True)),
                ('state', models.CharField(blank=True, max_length=255, null=True)),
                ('county', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=10, max_digits=13, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=10, max_digits=13, null=True)),
                ('nearest_place', models.TextField(blank=True, null=True)),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='location', to='place.place')),
            ],
        ),
        migrations.CreateModel(
            name='InterestingFacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interesting_fact', to='place.place')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.ImageField(default=None, upload_to='images/')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='place.place')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('places', models.ManyToManyField(blank=True, related_name='places', to='place.place', verbose_name='place')),
            ],
        ),
        migrations.CreateModel(
            name='FloraAndFauna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=255)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(default=None, upload_to='images/')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flora_fauna', to='place.place')),
            ],
        ),
        migrations.CreateModel(
            name='Entertainment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entertainment', to='place.place')),
            ],
        ),
        migrations.CreateModel(
            name='Cuisine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, default=None, max_digits=10)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='name', to='place.typecuisine')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cuisine', to='place.place')),
            ],
        ),
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='place_bookmark', to='place.place')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_bookmark', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AccommodationOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=255)),
                ('price', models.DecimalField(decimal_places=2, default=10, max_digits=13)),
                ('description', models.TextField(blank=True, null=True)),
                ('place', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='accommodation_Option', to='place.place')),
            ],
        ),
    ]

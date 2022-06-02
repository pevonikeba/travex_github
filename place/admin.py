from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
# Register your models here.
from django.contrib.admin import ModelAdmin, TabularInline
# from django.contrib.gis.admin import GISModelAdmin
# from modeltranslation.admin import TranslationAdmin
from mptt.admin import MPTTModelAdmin
from imagekit.admin import AdminThumbnail


# from geopy.geocoders import Nominatim
from achievement.admin import OwnedAchievementInline
from place import models
from place.models import Place, Group, PlaceImage, Transport, AccommodationOption, UniquenessPlace, MustSee, \
    WhereToTakeAPicture, ClimaticCondition, Safe, Cuisine, Entertainment, \
    NaturalPhenomena, \
    Vibe, FloraFauna, Category, UserPlaceRelation, InterestingFacts, CustomUser, GeographicalFeature, \
    PracticalInformation, TypeTransport, TypeCuisine, Location \


# admin.site.register(WorldBorder, admin.ModelAdmin)

class SafeInline(TabularInline):
    extra = 0
    model = Safe

class CuisineInline(TabularInline):
    extra = 0
    model = Cuisine

class EntertainmentInline(TabularInline):
    extra = 0
    model = Entertainment

class NaturalPhenomenaInline(TabularInline):
    extra = 0
    model = NaturalPhenomena

class LocationInline(TabularInline):
    extra = 0
    model = Location
    fk_name = "place"

class TransportInline(TabularInline):
    extra = 0
    model = Transport

class ImageInline(TabularInline):
    extra = 1
    model = PlaceImage

class AccommodationOptionsInline(TabularInline):
    extra = 0
    model = AccommodationOption

class UniquenessPlaceInline(TabularInline):
    extra = 0
    model = UniquenessPlace

class MustSeeInline(TabularInline):
    extra = 0
    model = MustSee

class VibeInline(TabularInline):
    extra = 0
    model = Vibe

class WhereToTakeAPictureInline(TabularInline):
    extra = 0
    model = WhereToTakeAPicture

class FloraFaunaInline(TabularInline):
    extra = 0
    model = FloraFauna

class InterestingFactsInline(TabularInline):
    extra = 0
    model = InterestingFacts

class PracticalInformationInline(TabularInline):
    extra = 0
    model = PracticalInformation


class PlaceInline(TabularInline):
    extra = 0
    model = Place
    fields = ('id', 'name', )
    readonly_fields = ('id', )

    def has_add_permission(self, request, obj):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

# class BookmarkInline(TabularInline):
#     extra = 0
#     model = Bookmark


# @admin.register(Transport)
# class TransportAdmin(TranslationAdmin):
#     group_fieldsets = True

@admin.register(Location)
class ImageAdmin(ModelAdmin):
    pass


@admin.register(PlaceImage)
class ImageAdmin(ModelAdmin):
    pass


@admin.register(Place)
class PlaceAdmin(ModelAdmin):
    save_on_top = True
    list_display = ('name', 'id', "home_page", "is_active", 'writer_user',)
    list_filter = ('home_page',)
    inlines = [ImageInline, LocationInline, SafeInline,  TransportInline, CuisineInline, AccommodationOptionsInline, UniquenessPlaceInline, VibeInline, MustSeeInline, EntertainmentInline, NaturalPhenomenaInline, WhereToTakeAPictureInline, InterestingFactsInline, PracticalInformationInline, FloraFaunaInline]

    # def save_model(self, request, obj, form, change):
    #
    #
    #
    #     geolocator = Nominatim(user_agent="geoapiExercises")
    #
    #     Latitude = str(obj.coordinate.coords[0])
    #     Longitude = str(obj.coordinate.coords[1])
    #     print('Latitude: ', Latitude)
    #     print('Longitude: ', Longitude)
    #     # Latitude = '37.862499'
    #     # Longitude = '58.238056'
    #
    #     location = geolocator.reverse(Latitude + "," + Longitude)
    #     # try:
    #
    #     print('obj: ', type(obj))
    #     print('obj: ', obj)
    #
    #     l = Location.objects.get_or_create(place=obj)
    #     print()
    #     print('LOCATION: ', l)
    #     l = l[0]
    #     print('LOCATION: ', l)
    #     print()
    #
    #     print(location.raw['address'])
    #     print(location.raw['lat'])
    #     print(location.raw['lon'])
    #
    #     if 'city' in location.raw['address']:
    #         l.city = location.raw['address']['city']
    #     if 'county' in location.raw['address']:
    #         l.city = location.raw['address']['county']
    #     if 'state' in location.raw['address']:
    #         l.region = location.raw['address']['state']
    #     if 'country' in location.raw['address']:
    #         l.country = location.raw['address']['country']
    #
    #     l.latitude = location.raw['lat']
    #     l.longitude = location.raw['lon']
    #
    #     l.save()
    #     # except:
    #     #     pass
    #
    #
    #
    #     # address = location.raw['address']
    #
    #     # print('address: ', address)
    #     # print('request: ', request)
    #     # print('obj: ', obj)
    #     # print('form', form)
    #     # print('change: ', change)
    #     # obj.user = request.user
    #     print("request.coordinate: ", obj.coordinate.coords[0])
    #     super().save_model(request, obj, form, change)


# @admin.register(NoActivePlace)
# class PlaceAdmin(ModelAdmin):
#     inlines = [ImageInline, LocationInline, SafeInline,  TransportInline, CuisineInline, AccommodationOptionsInline, UniquenessPlaceInline, VibeInline, MustSeeInline, EntertainmentInline, NaturalPhenomenaInline, WhereToTakeAPictureInline, InterestingFactsInline, PracticalInformationInline, FloraAndFaunaInline, BookmarkInline]


@admin.register(Group)
class GroupAdmin(ModelAdmin):
    pass

# admin.site.register(models.CustomUser, UserAdmin)


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    UserAdmin.fieldsets[1][1]['fields'] = UserAdmin.fieldsets[1][1]['fields'] + ('image',
                                                                                 'following',
                                                                                 'image_social',)
    list_display = ('pk', 'email', 'username', 'is_active', 'is_staff')
    list_display_links = ('email', )
    inlines = [OwnedAchievementInline]


class CategoryMPTTModelAdmin(MPTTModelAdmin):
    # specify pixel amount for this ModelAdmin only:
    mptt_level_indent = 20


admin.site.register(Category, CategoryMPTTModelAdmin)


@admin.register(UserPlaceRelation)
class UserPlaceRelationAdmin(ModelAdmin):
    pass


@admin.register(ClimaticCondition)
class ClimaticConditionAdmin(ModelAdmin):
    inlines = [PlaceInline, ]


@admin.register(GeographicalFeature)
class GeographicalFeatureAdmin(ModelAdmin):
    pass


@admin.register(TypeTransport)
class TypeTransportAdmin(ModelAdmin):
    readonly_fields = ('id',)

@admin.register(TypeCuisine)
class TypeCuisineAdmin(ModelAdmin):
    pass


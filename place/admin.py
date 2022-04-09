from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
# Register your models here.
from django.contrib.admin import ModelAdmin, TabularInline
from mptt.admin import MPTTModelAdmin

from place import models
from place.models import Place, Group, Image, Transport, AccommodationOptions, UniquenessPlace, MustSee, \
    WhereToTakeAPicture, Location, ClimaticConditions, Safe, Cuisine, Entertainment, \
    NaturalPhenomena, \
    Vibe, FloraAndFauna, Category, UserPlaceRelation, InterestingFacts, CustomUser, GeographicalFeature, \
    PracticalInformation, TypeTransport, TypeCuisine, Bookmark


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

class TransportInline(TabularInline):
    extra = 0
    model = Transport

class ImageInline(TabularInline):
    extra = 1
    model = Image

class AccommodationOptionsInline(TabularInline):
    extra = 0
    model = AccommodationOptions

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

class FloraAndFaunaInline(TabularInline):
    extra = 0
    model = FloraAndFauna

class InterestingFactsInline(TabularInline):
    extra = 0
    model = InterestingFacts

class PracticalInformationInline(TabularInline):
    extra = 0
    model = PracticalInformation

class BookmarkInline(TabularInline):
    extra = 0
    model = Bookmark


@admin.register(Place)
class PlaceAdmin(ModelAdmin):
    inlines = [ImageInline, LocationInline, SafeInline,  TransportInline, CuisineInline, AccommodationOptionsInline, UniquenessPlaceInline, VibeInline, MustSeeInline, EntertainmentInline, NaturalPhenomenaInline, WhereToTakeAPictureInline, InterestingFactsInline, PracticalInformationInline, FloraAndFaunaInline, BookmarkInline]

@admin.register(Group)
class GroupAdmin(ModelAdmin):
    pass

# admin.site.register(models.CustomUser, UserAdmin)


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    inlines = [BookmarkInline]

class CategoryMPTTModelAdmin(MPTTModelAdmin):
    # specify pixel amount for this ModelAdmin only:
    mptt_level_indent = 20

admin.site.register(Category, CategoryMPTTModelAdmin)

@admin.register(UserPlaceRelation)
class UserPlaceRelationAdmin(ModelAdmin):
    pass

@admin.register(ClimaticConditions)
class ClimaticConditionsAdmin(ModelAdmin):
    pass

@admin.register(GeographicalFeature)
class GeographicalFeatureAdmin(ModelAdmin):
    pass


@admin.register(TypeTransport)
class TypeTransportAdmin(ModelAdmin):
    pass

@admin.register(TypeCuisine)
class TypeCuisineAdmin(ModelAdmin):
    pass


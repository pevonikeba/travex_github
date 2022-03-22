from django.contrib import admin
from django.contrib.auth.models import User
# Register your models here.
from django.contrib.admin import ModelAdmin, TabularInline
from mptt.admin import MPTTModelAdmin

from place.models import Place, Group, Image, Transport, AccommodationOptions, UniquenessPlace, MustSee, \
    WhereToTakeAPicture, Location, ClimaticConditions, Safe, Cuisine, Entertainment, \
    NaturalPhenomena, \
    TypeOfTerrain, Vibe, FloraAndFauna, TypeOfPeople, Category, UserPlaceRelation


class SafeInline(TabularInline):
    extra = 1
    model = Safe

class CuisineInline(TabularInline):
    extra = 1
    model = Cuisine

class EntertainmentInline(TabularInline):
    extra = 1
    model = Entertainment

class NaturalPhenomenaInline(TabularInline):
    extra = 1
    model = NaturalPhenomena

class LocationInline(TabularInline):
    extra = 1
    model = Location

class TransportInline(TabularInline):
    extra = 1
    model = Transport

class ImageInline(TabularInline):
    extra = 1
    model = Image

class AccommodationOptionsInline(TabularInline):
    extra = 1
    model = AccommodationOptions

class UniquenessPlaceInline(TabularInline):
    extra = 1
    model = UniquenessPlace

class MustSeeInline(TabularInline):
    extra = 1
    model = MustSee

class VibeInline(TabularInline):
    extra = 1
    model = Vibe

class WhereToTakeAPictureInline(TabularInline):
    extra = 1
    model = WhereToTakeAPicture

class FloraAndFaunaInline(TabularInline):
    extra = 1
    model = FloraAndFauna


@admin.register(Place)
class PlaceAdmin(ModelAdmin):
    inlines = [ImageInline, LocationInline, SafeInline,  TransportInline, CuisineInline, AccommodationOptionsInline, UniquenessPlaceInline, VibeInline, MustSeeInline, EntertainmentInline, NaturalPhenomenaInline, WhereToTakeAPictureInline, FloraAndFaunaInline]

@admin.register(Group)
class GroupAdmin(ModelAdmin):
    pass

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

@admin.register(TypeOfTerrain)
class TypeOfTerrainAdmin(ModelAdmin):
    pass

@admin.register(TypeOfPeople)
class TypeOfPeopleAdmin(ModelAdmin):
    pass


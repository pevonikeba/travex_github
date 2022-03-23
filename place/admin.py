from django.contrib import admin
from django.contrib.auth.models import User
# Register your models here.
from django.contrib.admin import ModelAdmin, TabularInline
from mptt.admin import MPTTModelAdmin

from place.models import Place, Group, Image, Transport, AccommodationOptions, UniquenessPlace, MustSee, \
    WhereToTakeAPicture, Location, ClimaticConditions, Safe, Cuisine, Entertainment, \
    NaturalPhenomena, \
    TypeOfTerrain, Vibe, FloraAndFauna, TypeOfPeople, Category, UserPlaceRelation, InterestingFacts


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


@admin.register(Place)
class PlaceAdmin(ModelAdmin):
    inlines = [ImageInline, LocationInline, SafeInline,  TransportInline, CuisineInline, AccommodationOptionsInline, UniquenessPlaceInline, VibeInline, MustSeeInline, EntertainmentInline, NaturalPhenomenaInline, WhereToTakeAPictureInline, InterestingFactsInline, FloraAndFaunaInline]

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


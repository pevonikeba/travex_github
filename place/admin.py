from django.contrib import admin
from django.contrib.auth.models import User
# Register your models here.
from django.contrib.admin import ModelAdmin, TabularInline

from place.models import Place, Group, Image, Transport, AccommodationOptions, UniquenessPlace, MustSee, \
    WhereToTakeAPicture, Location, ClimaticConditions, Civilization, Safe, Turist, Cuisine, Entertainment, \
    NaturalPhenomena, \
    Socialization, TypeOfTerrain, Vibe


class CivilizationInline(TabularInline):
    extra = 1
    model = Civilization

class SafeInline(TabularInline):
    extra = 1
    model = Safe

class TuristInline(TabularInline):
    extra = 1
    model = Turist

class CuisineInline(TabularInline):
    extra = 1
    model = Cuisine

class EntertainmentInline(TabularInline):
    extra = 1
    model = Entertainment

class NaturalPhenomenaInline(TabularInline):
    extra = 1
    model = NaturalPhenomena

class SocializationInline(TabularInline):
    extra = 1
    model = Socialization

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



@admin.register(Place)
class PlaceAdmin(ModelAdmin):
    inlines = [ImageInline, LocationInline, CivilizationInline, SafeInline, TuristInline,  TransportInline, CuisineInline, AccommodationOptionsInline, UniquenessPlaceInline, SocializationInline, VibeInline, MustSeeInline, EntertainmentInline, NaturalPhenomenaInline, WhereToTakeAPictureInline]

@admin.register(Group)
class GroupAdmin(ModelAdmin):
    pass

@admin.register(ClimaticConditions)
class ClimaticConditionsAdmin(ModelAdmin):
    pass

@admin.register(TypeOfTerrain)
class TypeOfTerrainAdmin(ModelAdmin):
    pass


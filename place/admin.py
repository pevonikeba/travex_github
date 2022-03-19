from django.contrib import admin
from django.contrib.auth.models import User
# Register your models here.
from django.contrib.admin import ModelAdmin, TabularInline

from place.models import Place, Group, Image, Transport, AccommodationOptions, UniquenessPlace, MustSee, WhereToTakeAPicture


class TransportInline(TabularInline):
    model = Transport

class ImageInline(TabularInline):
    model = Image

class AccommodationOptionsInline(TabularInline):
    model = AccommodationOptions

class UniquenessPlaceInline(TabularInline):
    model = UniquenessPlace

class MustSeeInline(TabularInline):
    model = MustSee

class WhereToTakeAPictureInline(TabularInline):
    model = WhereToTakeAPicture

@admin.register(Place)
class PlaceAdmin(ModelAdmin):
    inlines = [ImageInline, TransportInline, AccommodationOptionsInline, UniquenessPlaceInline, MustSeeInline, WhereToTakeAPictureInline]

@admin.register(Group)
class GroupAdmin(ModelAdmin):
    pass


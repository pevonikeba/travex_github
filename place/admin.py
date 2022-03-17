from django.contrib import admin
from django.contrib.auth.models import User
# Register your models here.
from django.contrib.admin import ModelAdmin, TabularInline

from place.models import Place, Group, Image, Transport, AccommodationOptions, UniquenessPlace, MustSee, WhereToTakeAPicture


class ImageInline(TabularInline):
    model = Image

@admin.register(Place)
class PlaceAdmin(ModelAdmin):
    inlines = [ImageInline]

@admin.register(Group)
class GroupAdmin(ModelAdmin):
    pass

@admin.register(Transport)
class TransportAdmin(ModelAdmin):
    pass

@admin.register(AccommodationOptions)
class AccommodationOptionsAdmin(ModelAdmin):
    pass

@admin.register(UniquenessPlace)
class UniquenessPlaceAdmin(ModelAdmin):
    pass

@admin.register(MustSee)
class MustSeeAdmin(ModelAdmin):
    pass

@admin.register(WhereToTakeAPicture)
class WhereToTakeAPictureAdmin(ModelAdmin):
    pass


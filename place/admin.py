from django.contrib import admin
from django.contrib.auth.models import User
# Register your models here.
from django.contrib.admin import ModelAdmin, TabularInline

from place.models import Place, Group, Image

class ImageInline(TabularInline):
    model = Image

@admin.register(Place)
class PlaceAdmin(ModelAdmin):
    inlines = [ImageInline]

@admin.register(Group)
class GroupAdmin(ModelAdmin):
    pass


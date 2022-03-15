from django.contrib import admin
from django.contrib.auth.models import User
# Register your models here.
from django.contrib.admin import ModelAdmin

from place.models import Place, Groups


@admin.register(Place)
class PlaceAdmin(ModelAdmin):
    pass

@admin.register(Groups)
class GroupAdmin(ModelAdmin):
    pass


from django.contrib import admin
from django.contrib.gis import admin as gis_admin
from django.contrib.admin.options import FORMFIELD_FOR_DBFIELD_DEFAULTS

from location.models import PlaceLocation, UserLocation


@admin.register(PlaceLocation)
class PlaceLocationAdmin(admin.ModelAdmin):
    pass


@admin.register(UserLocation)
class UserLocationAdmin(admin.ModelAdmin):
    pass


class PlaceLocationInline(gis_admin.OSMGeoAdmin, gis_admin.TabularInline):
    extra = 0
    model = PlaceLocation
    fk_name = "place"

    def __init__(self, parent_model, admin_site):
        self.admin_site = admin_site
        self.parent_model = parent_model
        self.opts = self.model._meta
        self.has_registered_model = admin_site.is_registered(self.model)
        overrides = FORMFIELD_FOR_DBFIELD_DEFAULTS.copy()
        overrides.update(self.formfield_overrides)
        self.formfield_overrides = overrides
        if self.verbose_name is None:
            self.verbose_name = self.model._meta.verbose_name
        if self.verbose_name_plural is None:
            self.verbose_name_plural = self.model._meta.verbose_name_plural


class UserLocationInline(gis_admin.OSMGeoAdmin, gis_admin.TabularInline):
    extra = 0
    model = UserLocation
    fk_name = "writer_user"

    def __init__(self, parent_model, admin_site):
        self.admin_site = admin_site
        self.parent_model = parent_model
        self.opts = self.model._meta
        self.has_registered_model = admin_site.is_registered(self.model)
        overrides = FORMFIELD_FOR_DBFIELD_DEFAULTS.copy()
        overrides.update(self.formfield_overrides)
        self.formfield_overrides = overrides
        if self.verbose_name is None:
            self.verbose_name = self.model._meta.verbose_name
        if self.verbose_name_plural is None:
            self.verbose_name_plural = self.model._meta.verbose_name_plural

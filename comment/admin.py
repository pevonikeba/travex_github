from django.contrib import admin

from comment.models import PlaceComment, SubPlaceComment


@admin.register(PlaceComment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('place', 'name', 'body', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


@admin.register(SubPlaceComment)
class SubCommentAdmin(admin.ModelAdmin):
    list_display = ('place_comment', 'name', 'body', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
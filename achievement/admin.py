from django.contrib import admin

from achievement.models import Achievement, OwnedAchievement


@admin.register(Achievement)
class Achievement(admin.ModelAdmin):
    pass


class OwnedAchievementInline(admin.TabularInline):
    model = OwnedAchievement

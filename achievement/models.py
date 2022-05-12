from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from place.models import CustomUser


class Achievement(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/achievements/', null=True, blank=True)
    how_to_own = models.TextField(blank=True)
    level_increase_to = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    owner = models.ManyToManyField(CustomUser, through='OwnedAchievement')

    def __str__(self):
        return self.title


class OwnedAchievement(models.Model):
    writer_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)
    level = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('writer_user', 'achievement',)

    def __str__(self):
        return f"{self.writer_user}: {self.achievement}: {self.level}"
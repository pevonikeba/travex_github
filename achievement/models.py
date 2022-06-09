from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# from place.models import CustomUser


class Achievement(models.Model):
    ACHIEVEMENT_TITLE_CHOICES = (
        ('Register', 'Register'),
        ('Posting 1', 'Posting 1'),
        ('Posting 3', 'Posting 3'),
        ('Posting 5', 'Posting 5'),
        ('Travel destination 3', 'Travel destination 3'),
        ('Travel destination 5', 'Travel destination 5'),
        ('Travel destination 7', 'Travel destination 7'),
        ('Stranger', 'Stranger'),
        ('Yeti', 'Yeti'),
    )
    title = models.CharField(max_length=255, choices=ACHIEVEMENT_TITLE_CHOICES, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/achievements/', null=True, blank=True)
    how_to_own = models.TextField(blank=True)
    level_increase_to = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    owner = models.ManyToManyField('place.CustomUser', through='OwnedAchievement', related_name='achievements')


    def __str__(self):
        return f'{self.title}: level increase to -> {self.level_increase_to}'


class OwnedAchievement(models.Model):
    writer_user = models.ForeignKey('place.CustomUser', on_delete=models.CASCADE)
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('writer_user', 'achievement',)

    def __str__(self):
        return f"{self.writer_user}: {self.achievement}"
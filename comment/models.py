from django.db import models

from place.models import Place, CustomUser


class CommentAbstract(models.Model):
    name = models.CharField(max_length=80)
    writer_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=False)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        abstract = True
        ordering = ['-created_on']

    def __str__(self):
        return f'Comment {self.body} by {self.name}'


class PlaceComment(CommentAbstract):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='place_comments')


class SubPlaceComment(CommentAbstract):
    place_comment = models.ForeignKey(PlaceComment, on_delete=models.CASCADE, related_name='sub_place_comments')
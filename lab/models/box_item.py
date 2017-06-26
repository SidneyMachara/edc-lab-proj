from django.db import models
from django.db.models.deletion import PROTECT

from .box import Box


class BoxItem(models.Model):

    box = models.ForeignKey(Box, on_delete=PROTECT)

    position = models.IntegerField()

    identifier = models.CharField(
        max_length=25)

    comment = models.CharField(
        max_length=25,
        null=True,
        blank=True)

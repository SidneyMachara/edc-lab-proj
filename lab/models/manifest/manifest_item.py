from django.db import models
from django.db.models import PROTECT
from .manifest import Manifest


class ManifestItem(models.Model):

    manifest = models.ForeignKey(Manifest, on_delete=PROTECT)

    identifier = models.CharField(
        max_length=25)

    comment = models.CharField(
        max_length=25,
        null=True,
        blank=True)

    objects = models.Manager()

    def human_readable_identifier(self):
        x = self.identifier
        return '{}-{}-{}'.format(x[0:4], x[4:8], x[8:12])

    class Meta:
        app_label = 'lab'
        unique_together = ('manifest', 'identifier')

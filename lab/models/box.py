from django.db import models
from django.utils import timezone
from django.db.models import PROTECT
from ..constants import TESTING, STORAGE, DAMAGED, OTHER, OPEN
from .box_type import BoxType
from ..identifiers import BoxIdentifier

BOX_CATEGORY = (
    (TESTING, 'Testing'),
    (STORAGE, 'Storage'),
    (OTHER, 'Other'),
)

STATUS = (
    (OPEN, 'Open'),
    (DAMAGED, 'Damaged'),
)


class Box(models.Model):

    box_identifier = models.CharField(
        max_length=25,
        editable=False,
        unique=True)

    name = models.CharField(
        max_length=25,
        null=True,
        blank=True)

    box_type = models.ForeignKey(
        BoxType, on_delete=PROTECT)

    box_datetime = models.DateTimeField(
        default=timezone.now)

    category = models.CharField(
        max_length=25,
        default=TESTING,
        choices=BOX_CATEGORY)

    category_other = models.CharField(
        max_length=25,
        null=True,
        blank=True)

    specimen_types = models.CharField(
        max_length=25,
        help_text=(
            'List of specimen types in this box. Use two-digit numeric '
            'codes separated by commas.'))

    status = models.CharField(
        max_length=15,
        default=OPEN,
        choices=STATUS)

    accept_box = models.BooleanField(
        default=False,
        help_text='Tick to accept/decline this box')

    comment = models.TextField(
        null=True,
        blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.name

    def count(self):
        return self.boxitem_set.all().count()

    def items(self):
        return self.boxitem_set.all().order_by('position')

    @property
    def human_readable_identifier(self):
        x = self.box_identifier
        return '{}-{}-{}'.format(x[0:4], x[4:8], x[8:12])

    @property
    def next_position(self):
        """Returns an integer or None.
        """
        last_obj = self.boxitem_set.all().order_by('position').last()
        if not last_obj:
            next_position = 1
        else:
            next_position = last_obj.position + 1
        if next_position > self.box_type.total:
            next_position = None
        return next_position

#     @property
#     def max_position(self):
#         return

    def save(self, *args, **kwargs):
        if not self.box_identifier:
            identifier = BoxIdentifier(model=self.__class__)
            self.identifier = identifier.identifier
        if not self.name:
            self.name = self.box_identifier
        super().save(*args, **kwargs)

    class Meta:
        app_label = 'lab'
#         ordering = ('-box_datetime', )
        verbose_name_plural = 'Boxes'

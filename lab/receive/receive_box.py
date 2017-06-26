from lab.models.box import Box
from django.utils import timezone


class BoxRejected(Exception):
    pass


class ReceiveBox:

    def __init__(self, box=None, manifest=None):
        self.box = box
        self.manifest = manifest
        if not self.box:
            raise BoxRejected(
                f'The box is rejected because it is not in good condition'
                f'Box status is {box.status}')
        self.accept_box()

    def is_box_valid(self):
        return isinstance(self.box, Box)

    def is_box_datetime_valid(self):
        now = timezone.now()
        dateCheck = False
        if self.manifest.manifest_datetime <= now:
            if self.box.box_datetime <= self.manifest.manifest_datetime:
                dateCheck = True

        return dateCheck

    def is_box_items_count_equal_manifest_item_count(self):

        box_item = self.box.count()
        manifest_item = self.manifest.count()

        return box_item == manifest_item

    def accept_box(self):
        if self.is_box_items_count_equal_manifest_item_count() and\
                self.is_box_datetime_valid():
            self.box.accept_box = True
            self.box.save()

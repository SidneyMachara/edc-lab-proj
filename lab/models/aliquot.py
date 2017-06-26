from ..model_mixins import AliquotModelMixin
from ..model_mixins  import AliquotIdentifierModelMixin
from ..model_mixins import AliquotTypeModelMixin

from django.db import models


class Aliquot(AliquotModelMixin, AliquotIdentifierModelMixin, 
              AliquotTypeModelMixin):
    objects = models.Manager()
    
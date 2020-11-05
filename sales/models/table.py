# django
from django.db import models
from django.utils.translation import ugettext_lazy as _

# base
from base.models import BaseModel


class Table(BaseModel):
    number = models.PositiveSmallIntegerField(
        _('number'),
    )

    class Meta:
        ordering = (
            'number',
        )

    def __str__(self):
        return str(self.number)

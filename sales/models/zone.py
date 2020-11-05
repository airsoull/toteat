# django
from django.db import models
from django.utils.translation import ugettext_lazy as _

# base
from base.models import BaseModel


class Zone(BaseModel):
    name = models.CharField(
        _('name'),
        max_length=255,
    )

    class Meta:
        ordering = (
            'name',
        )

    def __str__(self):
        return self.name

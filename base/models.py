# django
from django.db import models
from django.utils.translation import ugettext_lazy as _


class BaseModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('created at'),
    )
    updated_at = models.DateTimeField(
        auto_now=True, null=True,
        verbose_name=_('updated at'),
    )

    class Meta:
        abstract = True

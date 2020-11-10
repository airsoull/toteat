# standard library
import json

# django
from django.core.serializers.json import DjangoJSONEncoder
from django.db import models
from django.db.models import Count


class QuerySet(models.query.QuerySet):
    def to_json(self):
        return json.dumps(list(self.values()), cls=DjangoJSONEncoder)

    def find_duplicates(self, *fields):
        duplicates = self.values(*fields).annotate(Count('id'))
        return duplicates.order_by().filter(id__count__gt=1)

    def related_objects(self):
        return self.select_related(
            *(f.name for f in self.model._meta.fields if f.is_relation)
        )

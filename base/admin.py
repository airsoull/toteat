from django.contrib import admin


class BaseModelAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.select_related(
            *(f.name for f in queryset.model._meta.fields if f.is_relation)
        )
        return queryset

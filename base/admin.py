from django.contrib import admin


class BaseModelAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.related_objects()
        return queryset

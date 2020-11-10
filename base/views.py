# django
from django.views.generic import ListView
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


class BaseListView(LoginRequiredMixin, ListView):
    pass


class BaseDetailView(LoginRequiredMixin, DetailView):
    pass

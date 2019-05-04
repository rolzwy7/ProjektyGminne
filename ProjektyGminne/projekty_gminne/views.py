from django.shortcuts import render

from django.views import generic
from django.shortcuts import render, reverse
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_GET
from . import models

from django.db.models import Q
from django.utils import timezone


class SearchTool(generic.View):
    template_name = "projekty_gminne/search.html"

    @method_decorator(require_GET)
    def get(self, request):
        data = {}
        data["dzielnice"] = models.Dzielnica.objects.all()
        return render(request, self.template_name, {"data": data})


class AktywneKonkursyList(generic.ListView):
    template_name = "projekty_gminne/aktywne_konkursy_list.html"
    model = models.Konkurs
    paginate_by = 15
    title = "Aktywne Konkursy"

    def get_queryset(self):
        context = models.Konkurs.objects.filter(
            Q(date_start__lt=timezone.now()) &
            Q(date_finish__gt=timezone.now())
        )
        return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.title
        return context


class ZakonczoneKonkursyList(generic.ListView):
    template_name = "projekty_gminne/zakonczone_konkursy_list.html"
    model = models.Konkurs
    paginate_by = 15
    title = "Zakończone Konkursy"

    def get_queryset(self):
        context = models.Konkurs.objects.filter(
            Q(date_finish__lt=timezone.now())
        )
        return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.title
        return context


class WszystkieKonkursyList(generic.ListView):
    template_name = "projekty_gminne/wszystkie_konkursy_list.html"
    model = models.Konkurs
    paginate_by = 15
    title = "Wszystkie Konkursy"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.title
        return context

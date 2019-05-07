from django.shortcuts import render

from django.views import generic
from django.shortcuts import render, reverse
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_GET
from . import models
from django import http
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

from django.db.models import Q
from django.utils import timezone


class AktywneKonkursyList(generic.ListView):
    template_name = "projekty_gminne/aktywne_konkursy_list.html"
    model = models.Konkurs
    paginate_by = 10
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

    def get_queryset(self):
        try:
            name = self.request.GET['nazwa']
        except Exception as e:
            context = self.model.objects.all()
        else:
            context = self.model.objects.filter(name__icontains=name)
        finally:
            return context


class ZakonczoneKonkursyList(generic.ListView):
    template_name = "projekty_gminne/zakonczone_konkursy_list.html"
    model = models.Konkurs
    paginate_by = 10
    title = "Zakończone Konkursy"

    def get_queryset(self):
        context = self.model.objects.filter(
            Q(date_finish__lt=timezone.now())
        )
        return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.title
        return context

    def get_queryset(self):
        try:
            name = self.request.GET['nazwa']
        except Exception as e:
            context = self.model.objects.all()
        else:
            context = self.model.objects.filter(name__icontains=name)
        finally:
            return context


class WszystkieKonkursyList(generic.ListView):
    template_name = "projekty_gminne/wszystkie_konkursy_list.html"
    model = models.Konkurs
    paginate_by = 10
    title = "Wszystkie Konkursy"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.title
        return context

    def get_queryset(self):
        try:
            name = self.request.GET['nazwa']
        except Exception as e:
            context = self.model.objects.all()
        else:
            context = self.model.objects.filter(name__icontains=name)
        finally:
            return context


class KonkursDetail(generic.DetailView):
    template_name = "projekty_gminne/konkurs_detail.html"
    model = models.Konkurs
    title = "Strona Konkursu"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Konkurs: %s" % self.title
        return context


class ProjektDetail(generic.DetailView):
    template_name = "projekty_gminne/projekt_detail.html"
    model = models.Projekt
    title = "Strona Projektu"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Projekt: %s" % self.title

        context["active"] = False
        if context["object"].konkurs_id.date_start < timezone.now():
            if context["object"].konkurs_id.date_finish > timezone.now():
                context["active"] = True

        return context


@csrf_exempt
def glosuj_ajax(request):
    if request.method != "POST":
        return http.HttpResponseNotAllowed(["POST"])
    post_ = json.loads(request.body)
    projekt_id = post_.get("project_id")
    pesel = post_.get("pesel")
    if pesel is None or projekt_id is None:
        return http.HttpResponseBadRequest()
    if not isinstance(projekt_id, int):
        return http.HttpResponseBadRequest()
    # check if pesel correct (in db)
    # models.
    # save vote
    return http.HttpResponse("OK")

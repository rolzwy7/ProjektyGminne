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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.title
        return context

    def get_queryset(self):
        try:
            name = self.request.GET['nazwa']
        except Exception as e:
            context = models.Konkurs.objects.filter(
                Q(date_start__lt=timezone.now()) &
                Q(date_finish__gt=timezone.now())
            )
        else:
            context = self.model.objects.filter(
                Q(name__icontains=name) &
                Q(date_start__lt=timezone.now()) &
                Q(date_finish__gt=timezone.now())
            )
        finally:
            return context


class ZakonczoneKonkursyList(generic.ListView):
    template_name = "projekty_gminne/zakonczone_konkursy_list.html"
    model = models.Konkurs
    paginate_by = 10
    title = "Zakończone Konkursy"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.title
        return context

    def get_queryset(self):
        try:
            name = self.request.GET['nazwa']
        except Exception as e:
            context = self.model.objects.filter(
                Q(date_finish__lt=timezone.now())
            )
        else:
            context = self.model.objects.filter(
            Q(name__icontains=name) &
            Q(date_finish__lt=timezone.now())
            )
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

        context["active"] = False
        if context["object"].date_start < timezone.now():
            if context["object"].date_finish > timezone.now():
                context["active"] = True

        if context["active"]:
            self.template_name = "projekty_gminne/konkurs_active_detail.html"
            context["projekty_list"] = models.Projekt.objects.filter(konkurs_id=context["object"])
        else:
            self.template_name = "projekty_gminne/konkurs_inactive_detail.html"

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

        # count votes
        context["vote_count"] = models.Glos.objects.filter(projekt_id=context["object"]).count()

        # other projects
        context["other_projects"] = models.Projekt.objects.filter(konkurs_id=context["object"].konkurs_id)

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

    # Check if already voted
    glos_count = models.Glos.objects.filter(name=pesel, projekt_id=projekt_id).count()
    json_response = {
        "msg": "Głos został już oddany za pomocą tego numer PESEL",
        "success": False,
        "voted_before": True
    }
    if glos_count != 0:
        return http.JsonResponse(json_response)

    # check if pesel correct (in db)
    projekt_obj = models.Projekt.objects.filter(id=projekt_id)

    # projket nie istnieje
    if projekt_obj.count() != 1:
        return http.HttpResponseBadRequest()

    # czy glos zostal oddany na inne projekty w konkursie
    other_proj = models.Glos.objects.filter(name=pesel, projekt_id__konkurs_id=projekt_obj[0].konkurs_id)
    if other_proj.count() != 0:
        json_response = {
            "msg": "Głos został już oddany na inny projekt w ramach tego konkursu",
            "success": False
        }
        return http.JsonResponse(json_response)

    # check if konkurs active
    konkurs_active = False
    if projekt_obj[0].konkurs_id.date_start < timezone.now():
        if projekt_obj[0].konkurs_id.date_finish > timezone.now():
            konkurs_active = True
    if not konkurs_active:
        json_response = {
            "msg": "Konkurs został zakończony",
            "success": False
        }
        return http.JsonResponse(json_response)

    dzielnica_obj = projekt_obj[0].konkurs_id.dzielnica_id
    pesel_obj = models.ApiMockData.objects.filter(pesel=pesel)

    # pesel nei istnieje
    if pesel_obj.count() != 1:
        json_response = {
            "msg": "Niepoprawny numer PESEL",
            "success": False
        }
        return http.JsonResponse(json_response)

    pesel_valid = False
    if pesel_obj[0].dzielnica_id.id == dzielnica_obj.id:
        pesel_valid = True

    # save vote
    if pesel_valid:
        vote_obj = models.Glos(name=pesel, projekt_id=projekt_obj[0])
        vote_obj.save()
        json_response = {
            "msg": "Głos został zapisany",
            "success": True
        }
        return http.JsonResponse(json_response)
    else:
        json_response = {
            "msg": "Niepoprawne miejsce zamieszkania. Brak uprawnień do oddania głosu",
            "success": False
        }
        return http.JsonResponse(json_response)

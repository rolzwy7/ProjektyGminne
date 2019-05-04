from django.views import generic
from django.shortcuts import render, reverse
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_GET

# REST framework
from rest_framework import viewsets
from . import serializers
from projekty_gminne import models
from django.db.models import Q
from django.utils import timezone


class ApiMockDataViewSet(viewsets.ModelViewSet):
    queryset = models.ApiMockData.objects.all()
    serializer_class = serializers.ApiMockDataSerializer


class GminaViewSet(viewsets.ModelViewSet):
    queryset = models.Gmina.objects.all()
    serializer_class = serializers.GminaSerializer


class DzielnicaViewSet(viewsets.ModelViewSet):
    queryset = models.Dzielnica.objects.all()
    serializer_class = serializers.DzielnicaSerializer


class GlosViewSet(viewsets.ModelViewSet):
    queryset = models.Glos.objects.all()
    serializer_class = serializers.GlosSerializer


class AktywneKonkursyViewSet(viewsets.ModelViewSet):
    queryset = models.Konkurs.objects.filter(
        Q(date_start__lt=timezone.now()) & Q(date_finish__gt=timezone.now()))
    serializer_class = serializers.AktywneKonkursySerializer


class ZakonczoneKonkursyViewSet(viewsets.ModelViewSet):
    queryset = models.Konkurs.objects.filter(
        Q(date_finish__lt=timezone.now()))
    serializer_class = serializers.ZakonczoneKonkursySerializer


class Homepage(generic.View):
    template_name = "_Main/homepage.html"

    @method_decorator(require_GET)
    def get(self, request):
        data = {}
        return render(request, self.template_name, {"data": data})

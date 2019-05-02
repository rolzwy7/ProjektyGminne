from django.views import generic
from django.shortcuts import render, reverse
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_GET

# REST framework
from rest_framework import viewsets
from .serializers import ApiMockDataSerializer
from .serializers import GminaSerializer
from .serializers import DzielnicaSerializer
from projekty_gminne.models import ApiMockData, Dzielnica, Gmina


class ApiMockDataViewSet(viewsets.ModelViewSet):
    queryset = ApiMockData.objects.all()
    serializer_class = ApiMockDataSerializer


class GminaViewSet(viewsets.ModelViewSet):
    queryset = Gmina.objects.all()
    serializer_class = GminaSerializer


class DzielnicaViewSet(viewsets.ModelViewSet):
    queryset = Dzielnica.objects.all()
    serializer_class = DzielnicaSerializer


class Homepage(generic.View):
    template_name = "_Main/homepage.html"

    @method_decorator(require_GET)
    def get(self, request):
        return render(request, self.template_name, {})

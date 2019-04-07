from django.views import generic
from django.shortcuts import render, reverse
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_GET


class Homepage(generic.View):
    template_name = "_Main/homepage.html"

    @method_decorator(require_GET)
    def get(self, request):
        return render(request, self.template_name, {})

from django.contrib import admin
from projekty_gminne import models


@admin.register(models.Konkurs)
class KonkursAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'is_active']

    def is_active(self, obj):
        return obj.is_active()
    is_active.boolean = True


@admin.register(models.Gmina)
class GminaAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Dzielnica)
class DzielnicaAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Projekt)
class ProjektAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Glos)
class GlosAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ApiMockData)
class ApiMockDataAdmin(admin.ModelAdmin):
    list_display = ['pesel', 'dzielnica_id']

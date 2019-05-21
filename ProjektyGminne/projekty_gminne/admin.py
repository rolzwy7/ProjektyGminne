from django.contrib import admin
from ProjektyGminne.admin import admin_site
from projekty_gminne import models
from django.utils import timezone
from django.db.models import Q
from django.contrib.auth.models import User, Group


class IsKonkursActiveFilter(admin.SimpleListFilter):
    title = 'is_active'
    parameter_name = 'is_active'

    def lookups(self, request, model_admin):
        return (
            ('Yes', 'Yes'),
            ('No', 'No'),
        )

    def queryset(self, request, queryset):
        value = self.value()
        if value == 'Yes':
            return queryset.filter(
                Q(date_start__lt=timezone.now()) &
                Q(date_finish__gt=timezone.now())
            )
        elif value == 'No':
            return queryset.exclude(
                Q(date_start__lt=timezone.now()) &
                Q(date_finish__gt=timezone.now())
            )
        return queryset


class KonkursAdmin(admin.ModelAdmin):

    def f_date_start(self, obj):
        return obj.date_start.strftime("%Y/%m/%d %H:%M:%S")
    f_date_start.short_description = 'f_date_start'

    def f_date_finish(self, obj):
        return obj.date_finish.strftime("%Y/%m/%d %H:%M:%S")
    f_date_finish.short_description = 'f_date_finish'

    ordering = ['date_start']
    list_display = ['__str__', 'dogrywka', 'f_date_start', 'f_date_finish', 'is_active']
    list_filter = ['dogrywka', IsKonkursActiveFilter]
    search_fields = ['__str__']

    def is_active(self, obj):
        return obj.is_active()

    def dogrywka(self, obj):
        return obj.dogrywka

    is_active.boolean = True
    dogrywka.boolean = True


class GminaAdmin(admin.ModelAdmin):
    pass


class DzielnicaAdmin(admin.ModelAdmin):
    pass


class ProjektAdmin(admin.ModelAdmin):
    pass


class GlosAdmin(admin.ModelAdmin):
    pass


class ApiMockDataAdmin(admin.ModelAdmin):
    list_display = ['pesel', 'dzielnica_id']


admin_site.register(models.Konkurs, KonkursAdmin)
admin_site.register(models.Gmina, GminaAdmin)
admin_site.register(models.Dzielnica, DzielnicaAdmin)
admin_site.register(models.Projekt, ProjektAdmin)
admin_site.register(models.Glos, GlosAdmin)
admin_site.register(models.ApiMockData, ApiMockDataAdmin)


# ------------------------------- USER ------------------------
admin_site.register(User)
admin_site.register(Group)

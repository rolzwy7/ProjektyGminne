from django.contrib import admin
from django.urls import path, include, re_path
from ProjektyGminne import views
from django.conf.urls.static import static
from django.conf import settings
from projekty_gminne.admin import admin_site


from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'pesel_check', views.ApiMockDataViewSet, 'pesel_check')
router.register(r'dzielnica', views.DzielnicaViewSet, 'dzielnica')
router.register(r'glos', views.GlosViewSet, "glos")
router.register(r'gmina', views.GminaViewSet, 'gmina')
router.register(r'projekt', views.ProjektViewSet, 'projekt')
router.register(r'zakonczone_konkursy', views.ZakonczoneKonkursyViewSet, "zakonczone_konkursy")
router.register(r'aktywne_konkursy', views.AktywneKonkursyViewSet, "aktywne_konkursy")

urlpatterns = [
    # path('django_admin/', admin.site.urls),
    path('admin/', admin_site.urls),
    path('django_admin/', admin.site.urls),
    path('konkursy/', include('projekty_gminne.urls')),
    path('api/q/', include(router.urls)),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
    path('kfp/<int:pk>', views.ProjektyWKonkursie.as_view(), name="kfp"),
    re_path('^$', views.Homepage.as_view(), name="homepage"),
]

# Add media for development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

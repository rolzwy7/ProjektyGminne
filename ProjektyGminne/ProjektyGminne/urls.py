from django.contrib import admin
from django.urls import path, include, re_path
from ProjektyGminne import views
from django.conf.urls.static import static
from django.conf import settings


from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'pesel_check', views.ApiMockDataViewSet)
router.register(r'dzielnica', views.DzielnicaViewSet)
router.register(r'gmina', views.GminaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('konkursy/', include('projekty_gminne.urls')),

    path('api/q/', include(router.urls)),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),

    re_path('^$', views.Homepage.as_view(), name="homepage"),
]

# Add media for development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

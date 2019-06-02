
from django.urls import path, include
from projekty_gminne import views

urlpatterns = [
    # path('search', views.SearchTool.as_view(), name="search-tool"),
    path('aktywne/', views.AktywneKonkursyList.as_view(), name="konkursy-aktywne"),
    path('zakonczone/', views.ZakonczoneKonkursyList.as_view(), name="konkursy-zakonczone"),
    path('konkurs/<int:pk>', views.KonkursDetail.as_view(), name="konkurs-detail"),
    path('projekt/<int:pk>', views.ProjektDetail.as_view(), name="projekt-detail"),
    path('projekty/', views.WszystkieProjektyList.as_view(), name="projekt-listing"),
    path('vote', views.glosuj_ajax, name="glosuj-view"),
    path('', views.WszystkieKonkursyList.as_view(), name="konkursy-wszystkie"),
]

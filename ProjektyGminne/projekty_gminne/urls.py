
from django.urls import path, include
from projekty_gminne import views

urlpatterns = [
    path('search', views.SearchTool.as_view(), name="search-tool"),
    path('aktywne', views.AktywneKonkursyList.as_view(), name="konkursy-aktywne"),
    path('zakonczone', views.ZakonczoneKonkursyList.as_view(), name="konkursy-zakonczone"),
    path('wszystkie', views.WszystkieKonkursyList.as_view(), name="konkursy-wszystkie"),
]

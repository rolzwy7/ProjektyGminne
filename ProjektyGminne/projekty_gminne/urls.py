
from django.urls import path, include
from projekty_gminne import views

urlpatterns = [
    path('search', views.SearchTool.as_view(), name="search-tool"),
]

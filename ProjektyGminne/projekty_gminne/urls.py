
from django.urls import path, include
from projekty_gminne import views

urlpatterns = [
    path('', views.Homepage.as_view(), name="projekty-homepage"),
]

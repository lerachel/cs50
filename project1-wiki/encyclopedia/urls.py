from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>", views.check, name="check"),
    path("valid_entry", views.check, name="valid_entry")
]

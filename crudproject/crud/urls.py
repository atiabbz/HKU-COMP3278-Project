from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login, name="login"),
    path("notes", views.notes, name="notes"),
    path("notes/create", views.create, name="create"),
    path("notes/update", views.update, name="update"),
    path("notes/delete", views.delete, name="delete"),
    path("layout", views.layout, name="layout"),
    path("landing", views.landing, name="landing"),
]

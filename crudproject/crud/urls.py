from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("facial", views.facial, name="facial"),
    path("home", views.home, name="home"),
    path("logout", views.logout, name="logout"),
    path("transactions", views.transactions, name="transactions"),
    path("history", views.history, name="history"),
    path("settings", views.settings, name="settings"),
    path("login", views.login, name="login"),
    path("transfer", views.transfer, name="transfer"),
    path("updateDetails", views.updateDetails, name="updateDetails"),
    path('train', views.train_, name='train'),
    path("error", views.error, name="error"),
]

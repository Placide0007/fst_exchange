from django.urls import path

from . import views

urlpatterns = [
    path("", views.home,name="home"),
    path("profile/", views.profile,name="profile"),
    path("mathematics/", views.math,name="math"),
    path("pc/", views.pc,name="pc"),
]

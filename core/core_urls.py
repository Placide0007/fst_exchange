from django.urls import path

from . import views

urlpatterns = [
    path("", views.home,name="home"),
    path("profile/", views.profile,name="profile"),
    path("about/", views.about,name="about"),
    path("blog/", views.blog,name="blog"),
    path("blog/<int:post_id>/reaction/", views.react_post, name="react_post"),
]

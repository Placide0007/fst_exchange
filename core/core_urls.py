from django.urls import path

from . import views

urlpatterns = [
    path("", views.home,name="home"),
    path("profile/", views.profile,name="profile"),
    path("about/", views.about,name="about"),
    path('blog/', views.blog, name='blog'),
    path('<uuid:id>/', views.show, name='show'),
    path('react/<uuid:post_id>/', views.react_post, name='react_post'),
    path("blog/<uuid:post_id>/comment/", views.comment_post, name="comment_post"),
]
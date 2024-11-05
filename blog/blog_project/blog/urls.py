from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("create/", views.create_post, name="create_post"),
    path("posts/", views.posts_home, name="posts_home"),
    path("update/<int:post_id>/", views.update_post, name="update_post"),
]

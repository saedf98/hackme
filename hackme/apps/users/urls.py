from django.urls import path
from .views import UserView

app_name = "users"

urlpatterns = [
    path(
        "users/",
        UserView.as_view(template_name="users/index.html"),
        name="index",
    ),
    path(
        "users/create/",
        UserView.as_view(template_name="users/create.html"),
        name="create",
    ),
    path(
        "users/edit/<int:id>/",
        UserView.as_view(template_name="users/edit.html"),
        name="edit",
    ),
    path(
        "users/show/<int:id>/",
        UserView.as_view(template_name="users/show.html"),
        name="show",
    ),
]

from django.urls import path
from .views import UserView

app_name = "user"

urlpatterns = [
    path(
        "user/",
        UserView.as_view(template_name="profile/index.html"),
        name="index",
    ),
    # path(
    #     "user/create/",
    #     UserView.as_view(template_name="users/create.html"),
    #     name="create",
    # ),
    # path(
    #     "user/edit/<int:id>/",
    #     UserView.as_view(template_name="users/edit.html"),
    #     name="edit",
    # ),
    # path(
    #     "user/show/<int:id>/",
    #     UserView.as_view(template_name="users/show.html"),
    #     name="show",
    # ),
]

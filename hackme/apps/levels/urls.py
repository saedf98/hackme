from django.urls import path
from .views import LevelView

app_name = "levels"

urlpatterns = [
    path(
        "levels/",
        LevelView.as_view(template_name="levels/index.html"),
        name="index",
    ),
    path(
        "levels/create/",
        LevelView.as_view(template_name="levels/create.html"),
        name="create",
    ),
    path(
        "levels/edit/<int:id>/",
        LevelView.as_view(template_name="levels/edit.html"),
        name="edit",
    ),
    path(
        "levels/show/<int:id>/",
        LevelView.as_view(template_name="levels/show.html"),
        name="show",
    ),
]

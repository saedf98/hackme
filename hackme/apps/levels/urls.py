from django.urls import path
from .views import LevelView, LevelCreateView, LevelUpdateView, LevelDeleteView, LevelShowView

app_name = "levels"

urlpatterns = [
    path(
        "levels/",
        LevelView.as_view(template_name="levels/index.html"),
        name="index",
    ),
    path(
        "levels/create/",
        LevelCreateView.as_view(template_name="levels/create.html"),
        name="create",
    ),
    path(
        "levels/edit/<int:id>/",
        LevelUpdateView.as_view(template_name="levels/edit.html"),
        name="edit",
    ),
    path(
        "levels/show/<int:id>/",
        LevelShowView.as_view(template_name="levels/show.html"),
        name="show",
    ),
    path(
        "levels/delete/<int:id>/",
        LevelDeleteView.as_view(),
        name="delete",
    ),
]

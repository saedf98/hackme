from django.urls import path
from .views import LevelView


urlpatterns = [
    path(
        "levels/",
        LevelView.as_view(template_name="levels/index.html"),
        name="levels-index",
    ),
    path(
        "levels/create/",
        LevelView.as_view(template_name="levels/create.html"),
        name="levels-create",
    ),
    path(
        "levels/edit/<int:id>/",
        LevelView.as_view(template_name="levels/edit.html"),
        name="levels-edit",
    ),
]

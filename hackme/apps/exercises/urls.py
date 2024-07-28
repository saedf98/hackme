from django.urls import path
from .views import ExerciseView

app_name = "exercises"

urlpatterns = [
    path(
        "exercises/",
        ExerciseView.as_view(template_name="exercises/index.html"),
        name="index",
    ),
    path(
        "exercises/create/",
        ExerciseView.as_view(
            template_name="exercises/create.html"),
        name="create",
    ),
    path(
        "exercises/edit/<int:id>/",
        ExerciseView.as_view(
            template_name="exercises/edit.html"),
        name="edit",
    ),
    path(
        "exercises/show/<int:id>/",
        ExerciseView.as_view(
            template_name="exercises/show.html"),
        name="show",
    ),
]

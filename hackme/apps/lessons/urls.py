from django.urls import path
from .views import LessonView

app_name = "lessons"

urlpatterns = [
    path(
        "lessons/",
        LessonView.as_view(template_name="lessons/index.html"),
        name="index",
    ),
    path(
        "lessons/create/",
        LessonView.as_view(template_name="lessons/create.html"),
        name="create",
    ),
    path(
        "lessons/edit/<int:id>/",
        LessonView.as_view(template_name="lessons/edit.html"),
        name="edit",
    ),
    path(
        "lessons/show/<int:id>/",
        LessonView.as_view(template_name="lessons/show.html"),
        name="show",
    ),
]

from django.urls import path
from .views import LessonNoteView

app_name = "lesson_notes"

urlpatterns = [
    # path(
    #     "lesson_notes/",
    #     LessonNoteView.as_view(template_name="lesson_notes/index.html"),
    #     name="index",
    # ),
    path(
        "lesson_notes/create/",
        LessonNoteView.as_view(
            template_name="lesson_notes/create.html"),
        name="create",
    ),
    path(
        "lesson_notes/edit/<int:id>/",
        LessonNoteView.as_view(
            template_name="lesson_notes/edit.html"),
        name="edit",
    ),
    path(
        "lesson_notes/show/<int:id>/",
        LessonNoteView.as_view(
            template_name="lesson_notes/show.html"),
        name="show",
    ),
]

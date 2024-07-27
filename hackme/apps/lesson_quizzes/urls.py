from django.urls import path
from .views import LessonQuizView

app_name = "lesson_quizzes"

urlpatterns = [
    # path(
    #     "lesson_quizzes/",
    #     LessonQuizView.as_view(template_name="lesson_quizzes/index.html"),
    #     name="index",
    # ),
    path(
        "lesson_quizzes/create/",
        LessonQuizView.as_view(
            template_name="lesson_quizzes/create.html"),
        name="create",
    ),
    path(
        "lesson_quizzes/edit/<int:id>/",
        LessonQuizView.as_view(
            template_name="lesson_quizzes/edit.html"),
        name="edit",
    ),
    path(
        "lesson_quizzes/show/<int:id>/",
        LessonQuizView.as_view(
            template_name="lesson_quizzes/show.html"),
        name="show",
    ),
]

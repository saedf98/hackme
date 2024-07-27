from django.urls import path
from .views import CourseQuizView

app_name = "course_quizzes"

urlpatterns = [
    # path(
    #     "course_quizzes/",
    #     CourseQuizView.as_view(template_name="course_quizzes/index.html"),
    #     name="index",
    # ),
    path(
        "course_quizzes/create/",
        CourseQuizView.as_view(template_name="course_quizzes/create.html"),
        name="create",
    ),
    path(
        "course_quizzes/edit/<int:id>/",
        CourseQuizView.as_view(template_name="course_quizzes/edit.html"),
        name="edit",
    ),
    path(
        "course_quizzes/show/<int:id>/",
        CourseQuizView.as_view(template_name="course_quizzes/show.html"),
        name="show",
    ),
]

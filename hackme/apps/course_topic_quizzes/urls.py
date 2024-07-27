from django.urls import path
from .views import CourseTopicQuizView

app_name = "course_topic_quizzes"

urlpatterns = [
    # path(
    #     "course_topic_quizzes/",
    #     CourseTopicQuizView.as_view(template_name="course_topic_quizzes/index.html"),
    #     name="index",
    # ),
    path(
        "course_topic_quizzes/create/",
        CourseTopicQuizView.as_view(
            template_name="course_topic_quizzes/create.html"),
        name="create",
    ),
    path(
        "course_topic_quizzes/edit/<int:id>/",
        CourseTopicQuizView.as_view(
            template_name="course_topic_quizzes/edit.html"),
        name="edit",
    ),
    path(
        "course_topic_quizzes/show/<int:id>/",
        CourseTopicQuizView.as_view(
            template_name="course_topic_quizzes/show.html"),
        name="show",
    ),
]

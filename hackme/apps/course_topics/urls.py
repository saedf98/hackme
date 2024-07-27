from django.urls import path
from .views import CourseTopicView

app_name = "course_topics"

urlpatterns = [
    path(
        "course_topics/",
        CourseTopicView.as_view(template_name="course_topics/index.html"),
        name="index",
    ),
    path(
        "course_topics/create/",
        CourseTopicView.as_view(template_name="course_topics/create.html"),
        name="create",
    ),
    path(
        "course_topics/edit/<int:id>/",
        CourseTopicView.as_view(template_name="course_topics/edit.html"),
        name="edit",
    ),
    path(
        "course_topics/show/<int:id>/",
        CourseTopicView.as_view(template_name="course_topics/show.html"),
        name="show",
    ),
]

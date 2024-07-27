from django.urls import path
from .views import CourseView

app_name = "courses"

urlpatterns = [
    path(
        "courses/",
        CourseView.as_view(template_name="courses/index.html"),
        name="index",
    ),
    path(
        "courses/create/",
        CourseView.as_view(template_name="courses/create.html"),
        name="create",
    ),
    path(
        "courses/edit/<int:id>/",
        CourseView.as_view(template_name="courses/edit.html"),
        name="edit",
    ),
    path(
        "courses/show/<int:id>/",
        CourseView.as_view(template_name="courses/show.html"),
        name="show",
    ),
]

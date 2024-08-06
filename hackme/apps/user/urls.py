from django.urls import path
from .views import UserProfileView, UserCoursesView, UserMyCoursesView, UserCourseDetailsView, UserLessonView, UserExerciseView

app_name = "user"

urlpatterns = [
    path(
        "user/",
        UserProfileView.as_view(template_name="profile/index.html"),
        name="index",
    ),

    path(
        "user/courses",
        UserCoursesView.as_view(template_name="user/courses/index.html"),
        name="courses",
    ),
    path(
        "user/my-courses",
        UserMyCoursesView.as_view(
            template_name="user/courses/my-courses.html"),
        name="my-courses",
    ),
    path(
        "user/course-details/<int:id>",
        UserCourseDetailsView.as_view(
            template_name="user/courses/details.html"),
        name="course-details",
    ),
    path(
        "user/course/<int:id>/course-topic/<int:course_topic_id>/lesson/<int:lesson_id>",
        UserLessonView.as_view(
            template_name="user/lessons/index.html"),
        name="lesson",
    ),
    path(
        "user/course/<int:id>/course-topic/<int:course_topic_id>/lesson/<int:lesson_id>/exercises",
        UserExerciseView.as_view(
            template_name="user/exercises/index.html"),
        name="exercise",
    ),
    # path(
    #     "user/edit/<int:id>/",
    #     UserView.as_view(template_name="users/edit.html"),
    #     name="edit",
    # ),
    # path(
    #     "user/show/<int:id>/",
    #     UserView.as_view(template_name="users/show.html"),
    #     name="show",
    # ),
]

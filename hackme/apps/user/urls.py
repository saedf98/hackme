from django.urls import path
from .views import UserProfileView, AdminProfileView, UserCoursesView, UserMyCoursesView, UserCourseDetailsView, UserLessonView, UserExerciseView, UserAcademicDashboardView, UserCourseTopicQuizzesView, SubmitUserCourseTopicQuizzesView, UserRegisterCourseView, PasswordUpdateView, AdminPasswordUpdateView

app_name = "user"

urlpatterns = [
    path(
        "user",
        UserProfileView.as_view(template_name="profile/index.html"),
        name="index",
    ),
    path(
        "user/dashboard",
        UserAcademicDashboardView.as_view(
            template_name="user/dashboard/index.html"),
        name="dashboard",
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
        "user/course/<int:id>/register",
        UserRegisterCourseView.as_view(
            template_name="user/courses/register-course-first.html"),
        name="register-course-first",
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
    path(
        "user/course/<int:id>/course-topic/<int:course_topic_id>/lesson/<int:lesson_id>/quiz",
        UserCourseTopicQuizzesView.as_view(
            template_name="user/course_topic_quizzes/index.html"),
        name="course_topic_quiz",
    ),
    path(
        "user/register-course/<int:course_id>",
        UserCoursesView.as_view(template_name="user/courses/index.html"),
        name="register-course",
    ),
    path(
        "user/profile",
        UserProfileView.as_view(template_name="user/profile/index.html"),
        name="user-profile",
    ),
    path(
        "profile/password-update",
        PasswordUpdateView.as_view(template_name="user/profile/index.html"),
        name="password-update",
    ),
    path(
        "user/admin/profile",
        AdminProfileView.as_view(template_name="user/profile/index.html"),
        name="admin-profile",
    ),
    path(
        "user/admin/profile/password-update",
        AdminPasswordUpdateView.as_view(
            template_name="user/profile/index.html"),
        name="admin-password-update",
    ),
    path(
        "user/course-topic-quiz/submit",
        SubmitUserCourseTopicQuizzesView.as_view(),
        name="submit-course-topic-quiz",
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

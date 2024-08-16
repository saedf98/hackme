
from django.urls import reverse
from django.shortcuts import redirect
from apps.user_progress.models import UserCourses
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import UserPassesTestMixin


class HttpResponseUnauthorized(Exception):
    status_code = 401

# TODO(toheeb): make this permission based instead of role-based


class GroupRequiredMixin(UserPassesTestMixin):
    groups = []

    def test_func(self):
        # If groups is a string, convert it to a list
        if isinstance(self.groups, str):
            self.groups = [self.groups]
        return self.request.user.is_authenticated and any(self.request.user.groups.filter(name=group).exists() for group in self.groups)

    # TODO(toheeb): comeback to fix this properly
    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            return redirect(reverse("auth:login"))
        raise HttpResponseUnauthorized(
            "You do not have permission to access this page.")


class CourseRegistrationRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        course_id = self.kwargs.get('id')
        if not self.check_course_registration(request, course_id):
            return redirect('user:register-course-first', id=course_id)
        return super().dispatch(request, *args, **kwargs)

    def check_course_registration(self, request, course_id):
        user = request.user
        return UserCourses.objects.filter(user=user, course_id=course_id).exists()

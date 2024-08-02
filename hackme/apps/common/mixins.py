
from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import PermissionDenied


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

    #TODO(toheeb): comeback to fix this properly
    def handle_no_permission(self):
        raise HttpResponseUnauthorized(
            "You do not have permission to access this page.")

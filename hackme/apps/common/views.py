from django.urls import reverse_lazy
from apps.common.mixins import GroupRequiredMixin
from web_project import TemplateLayout
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from web_project.template_helpers.theme import TemplateHelper


"""
This file is a view controller for multiple pages as a module.
Here you can override the page view layout.
Refer to auth/urls.py file for more pages.
"""


class BlankView(TemplateView):
    # Predefined function
    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))

        # Update the context
        context.update(
            {
                "layout_path": TemplateHelper.set_layout("layout_blank.html", context),
            }
        )

        return context


class DashboardView(LoginRequiredMixin, GroupRequiredMixin, TemplateView):
    # login_url = '/auth/login'
    login_url = reverse_lazy('auth:login')
    groups = ['instructor', 'admin']

    # Predefined function
    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        context['user'] = self.request.user
        context['user_role'] = self.request.user.groups.all()[0].name

        return context


class UserDashboardView(LoginRequiredMixin, GroupRequiredMixin, TemplateView):
    # login_url = '/auth/login'
    login_url = reverse_lazy('auth:login')
    groups = ['user']

    # Predefined function
    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        context['user'] = self.request.user
        context['user_role'] = self.request.user.groups.all()[0].name

        return context

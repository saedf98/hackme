from apps.common.views import BlankView
from apps.courses.models import Course
from apps.lessons.models import Lesson
from apps.users.models import User
from django.views.generic import TemplateView
from apps.user.utils import format_number
from web_project import TemplateLayout

"""
This file is a view controller for multiple pages as a module.
Here you can override the page view layout.
Refer to dashboards/urls.py file for more pages.
"""


class DashboardsView(TemplateView):
    # Predefined function
    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))

        return context


class LandingPageView(BlankView):
    # Predefined function
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total_users = format_number(User.objects.count())
        total_courses = format_number(Course.objects.count())
        total_lessons = format_number(Lesson.objects.count())

        context.update({
            'total_users': total_users,
            'total_courses': total_courses,
            'total_lessons': total_lessons,
        })
        return context

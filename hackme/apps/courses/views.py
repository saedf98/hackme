from django.urls import reverse_lazy
from apps.common.views import DashboardView
from .models import Course
from .tables import CourseTable


# Create your views here.
class CourseView(DashboardView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        courses = CourseTable()
        # table = CourseTable(data=Course.objects.all())
        # Add more data to the context specific to this view
        context.update({
            "additional_data": "This is some additional data for MyView",
            "courses": courses,
            # Example of adding a URL to the context
            "some_url": reverse_lazy('some_named_url'),
        })

        return context

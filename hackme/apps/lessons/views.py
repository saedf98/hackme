from django.urls import reverse_lazy
from apps.common.views import DashboardView
from .models import Lesson
from .tables import LessonTable


# Create your views here.
class LessonView(DashboardView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        lessons = LessonTable()
        # table = LessonTable(data=Lesson.objects.all())
        # Add more data to the context specific to this view
        context.update({
            "additional_data": "This is some additional data for MyView",
            "lessons": lessons,
            # Example of adding a URL to the context
            "some_url": reverse_lazy('some_named_url'),
        })

        return context

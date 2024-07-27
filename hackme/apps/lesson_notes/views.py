from django.urls import reverse_lazy
from apps.common.views import DashboardView
from .models import LessonNote
from .tables import LessonNoteTable


# Create your views here.
class LessonNoteView(DashboardView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        lesson_notes = LessonNoteTable()
        # table = CourseTable(data=Course.objects.all())
        # Add more data to the context specific to this view
        context.update({
            "additional_data": "This is some additional data for MyView",
            "lesson_notes": lesson_notes,
            # Example of adding a URL to the context
            "some_url": reverse_lazy('some_named_url'),
        })

        return context

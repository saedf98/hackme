from django.urls import reverse_lazy
from apps.common.views import DashboardView
from .models import CourseTopicQuiz
from .tables import CourseTopicQuizTable


# Create your views here.
class CourseTopicQuizView(DashboardView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course_topic_quizzes = CourseTopicQuizTable()
        # table = CourseTable(data=Course.objects.all())
        # Add more data to the context specific to this view
        context.update({
            "additional_data": "This is some additional data for MyView",
            "course_topic_quizzes": course_topic_quizzes,
            # Example of adding a URL to the context
            "some_url": reverse_lazy('some_named_url'),
        })

        return context

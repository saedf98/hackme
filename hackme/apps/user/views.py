from django.urls import reverse_lazy
from django.contrib.contenttypes.models import ContentType
from apps.common.views import UserDashboardView
from django.views.generic import ListView
from apps.courses.models import Course
from apps.user_progress.models import UserCourses
from apps.lessons.models import Lesson


# Create your views here.
class UserView(UserDashboardView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        # Add more data to the context specific to this view
        context.update({
            "additional_data": "This is some additional data for MyView",
            "user": user,
            # Example of adding a URL to the context
            "some_url": reverse_lazy('some_named_url'),
        })

        return context


class UserProfileView(UserDashboardView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Add more data to the context specific to this view
        context.update({
            "additional_data": "This is some additional data for MyView",
            # Example of adding a URL to the context
            "some_url": reverse_lazy('some_named_url'),
        })

        return context


class UserCoursesView(UserDashboardView, ListView):
    model = Course
    object_list = Course.objects.all()
    context_object_name = 'courses'
    paginate_by = 10  # Number of items per page

    def get_queryset(self):
        # TODO: Customize your queryset if needed, will make it filter
        return Course.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course_count = Course.objects.count()
        app_labels = ['encryption_techniques',
                      'hashing_algorithms', 'digital_forensics']
        model_names = ['encryptiontechnique',
                       'hashingalgorithm', 'digitalforensic']
        course_content_types = ContentType.objects.filter(
            app_label__in=app_labels,
            model__in=model_names
        )

        # course_with_content_type = []
        # # Iterate over the courses in the queryset
        # for course in context['courses']:
        #     # Get the model class for the content_type
        #     model_class = course.content_type.model_class()
        #     # Fetch the related instance
        #     related_instance = model_class.objects.get(id=course.object_id)
        #     # Append detailed information to the list
        #     course_with_content_type.append({
        #         'course': course,
        #         'content_type': course.content_type,
        #         'related_instance': related_instance
        #     })

        # Add more data to the context specific to this view
        context.update({
            "additional_data": "This is some additional data for MyView",
            "course_count": course_count,
            "course_content_types": course_content_types,
            # Example of adding a URL to the context
            # "some_url": reverse_lazy('some_named_url'),
        })

        return context


class UserMyCoursesView(UserDashboardView):
    model = Course
    context_object_name = 'courses'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Add more data to the context specific to this view
        context.update({
            "additional_data": "This is some additional data for MyView",
            # Example of adding a URL to the context
            # "some_url": reverse_lazy('some_named_url'),
        })

        return context


class UserCourseDetailsView(UserDashboardView):
    model = Course
    context_object_name = 'courses'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course_id = self.kwargs.get('id')
        course = Course.objects.get(pk=course_id)
        # lessons = course.lessons.all()
        course_topics = course.course_topics.all()
        users_count = UserCourses.objects.filter(course=course).count()
        lessons_count = Lesson.objects.filter(course=course).count()
        total_duration = sum(
            lesson.duration for lesson in course.lessons.all())
        # Add more data to the context specific to this view
        context.update({
            # "lessons": lessons,
            "course": course,
            "lessons_count": lessons_count,
            "course_topics": course_topics,
            "users_count": users_count,
            "total_duration": total_duration

            # Example of adding a URL to the context
            # "some_url": reverse_lazy('some_named_url'),
        })

        return context

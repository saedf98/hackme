from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect
from .forms import LessonExerciseForm
from apps.lessons.models import Lesson
from apps.courses.models import Course
from django.views.generic import ListView
from apps.exercises.models import Exercise
from apps.common.views import UserDashboardView
from apps.user_progress.models import UserCourses
from django.contrib.contenttypes.models import ContentType


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

        # Add more data to the context specific to this view
        context.update({
            "additional_data": "This is some additional data for MyView",
            "course_count": course_count,
            "course_content_types": course_content_types,
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
        })

        return context


class UserCourseTopicsView(UserDashboardView):

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
        })

        return context


class UserCourseDetailsView(UserCourseTopicsView):
    model = Course
    context_object_name = 'courses'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class UserLessonView(UserCourseTopicsView):
    model = Lesson
    context_object_name = 'lessons'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course_topic_id = self.kwargs.get('course_topic_id')
        lesson_id = self.kwargs.get('lesson_id')
        lesson = Lesson.objects.get(pk=lesson_id)

        # Add more data to the context specific to this view
        context.update({
            "lesson": lesson,
            "lesson_id": lesson_id,
            "course_topic_id": course_topic_id
        })

        return context


class UserExerciseView(UserCourseTopicsView):
    model = Exercise
    context_object_name = 'exercises'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course_id = self.kwargs.get('id')
        course_topic_id = self.kwargs.get('course_topic_id')
        lesson_id = self.kwargs.get('lesson_id')
        lesson = Lesson.objects.get(pk=lesson_id)
        exercise = Exercise.objects.get(
            lesson=lesson_id,
            course=course_id)

        # Add more data to the context specific to this view
        context.update({
            "lesson": lesson,
            "exercise": exercise,
            "lesson_id": lesson_id,
            "course_topic_id": course_topic_id
        })

        return context

    def post(self, request, *args, **kwargs):

        redirect_url = request.META.get('HTTP_REFERER', '/')
        lesson_exercise_form = LessonExerciseForm(request.POST)
        if lesson_exercise_form.is_valid():
            exercise_id = lesson_exercise_form.cleaned_data['exercise_id']
            solution = lesson_exercise_form.cleaned_data['solution']
            solution_output = lesson_exercise_form.cleaned_data['solution_output']

            user_id = self.request.user.id
            exercise = Exercise.objects.get(pk=exercise_id)
            if exercise.answer != solution_output:
                messages.error(
                    request,
                    "Incorrect solution, go through the lesson again and comeback to the exercise solve!",
                    extra_tags='alert alert-danger alert-dismissible fade show')

                # TODO: check if solution is correct, if yes, mark lesson and exercise for user as completed
                # and save users solution 
            return redirect(redirect_url)

        messages.error(
            request, "Please solve the exercise before submission!",
            extra_tags='alert alert-danger alert-dismissible fade show')

        return redirect(redirect_url)
        # return HttpResponseRedirect("")

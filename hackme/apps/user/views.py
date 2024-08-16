from apps.user_progress.models import UserCourses, UserExercises, UserCourseTopics, UserLessons, UserCourseQuizzes, UserCourseTopicQuizzes, UserLessonQuizzes
import json
from django.http import JsonResponse
from django.urls import reverse
from django.db import transaction
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import redirect

from .forms import LessonExerciseForm
from apps.lessons.models import Lesson
from apps.courses.models import Course
from django.views.generic import ListView
from apps.exercises.models import Exercise
from apps.course_topics.models import CourseTopic
from django.shortcuts import get_object_or_404, redirect
from apps.common.mixins import CourseRegistrationRequiredMixin
from apps.common.views import UserDashboardView, DashboardView
from apps.course_topic_quizzes.models import CourseTopicQuiz
from django.contrib.contenttypes.models import ContentType
from .utils import create_user_exercise, create_user_lesson, get_completed_lessons_count, get_user_lesson_dict, get_registered_courses, count_users_registered_for_course, format_number, get_user_course_topic_quizzes, get_courses_total_duration, get_user_courses, get_user_courses_dict, check_course_registration


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


class AdminProfileView(DashboardView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Add more data to the context specific to this view
        context.update({
            "additional_data": "This is some additional data for MyView",
        })

        return context


class UserAcademicDashboardView(UserDashboardView):
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
        courses_duration = get_courses_total_duration()
        user_courses_dict = get_user_courses_dict(self.request.user)
        course_content_types = ContentType.objects.filter(
            app_label__in=app_labels,
            model__in=model_names
        )

        course_user_counts = {course.id: format_number(count_users_registered_for_course(
            course.id)) for course in self.object_list}
        registered_courses = get_registered_courses(self.request.user)

        context.update({
            "additional_data": "This is some additional data for MyView",
            "course_count": course_count,
            "courses_duration": courses_duration,
            "user_courses_dict": user_courses_dict,
            "registered_courses": registered_courses,
            "course_user_counts": course_user_counts,
            "course_content_types": course_content_types,
        })

        return context

    def post(self, request, course_id, *args, **kwargs):
        # course_id = self.kwargs.get('id')
        route_name = request.POST.get('route-name')
        user = request.user
        course = get_object_or_404(Course, id=course_id)
        if route_name == "register-course":
            if UserCourses.objects.filter(user=user, course=course).exists():
                messages.info(
                    self.request, f'You are already registered for the course: {course.name}.')
            else:
                # Register the user for the course
                UserCourses.objects.create(user=user, course=course)
                messages.success(
                    self.request, f'You have successfully registered for the course: {course.name}.')
        elif route_name == "start-over":
            try:
                with transaction.atomic():
                    UserLessons.objects.filter(
                        user=user, lesson__course=course).delete()
                    UserExercises.objects.filter(
                        user=user, exercise__course=course).delete()
                    UserCourseTopics.objects.filter(
                        user=user, course_topic__course=course).delete()
                    UserCourseQuizzes.objects.filter(
                        user=user, course_quiz__course=course).delete()
                    UserCourseTopicQuizzes.objects.filter(
                        user=user, course_topic_quiz__course=course).delete()
                    UserLessonQuizzes.objects.filter(
                        user=user, lesson_quiz__course=course).delete()
                    UserCourses.objects.filter(user=user, course=course).update(
                        completed=0, progress=0)
                messages.success(
                    request, f'Your progress for the course "{course.name}" has been successfully reset. You can now start over.')
            except Exception as e:
                messages.error(
                    request, f'An error occurred while resetting your progress for the course "{course.name}". Please try again.')

        return redirect(reverse("user:courses"))


class UserMyCoursesView(UserDashboardView):
    model = Course
    context_object_name = 'courses'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        courses_duration = get_courses_total_duration()
        my_courses = get_user_courses(self.request.user)

        # Add more data to the context specific to this view
        context.update({
            "my_courses": my_courses,
            "courses_duration": courses_duration,
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


class UserRegisterCourseView(UserDashboardView):
    model = Course
    context_object_name = 'courses'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course_id = self.kwargs.get('id')
        course = Course.objects.get(pk=course_id)
        course_topics = course.course_topics.all()
        users_count = UserCourses.objects.filter(course=course).count()
        lessons_count = Lesson.objects.filter(course=course).count()
        total_duration = sum(
            lesson.duration for lesson in course.lessons.all())
        completed_lessons_count = get_completed_lessons_count(
            self.request.user, course_id)
        user_lesson_dict = get_user_lesson_dict(self.request.user)

        context.update({
            "course": course,
            "lessons_count": lessons_count,
            "course_topics": course_topics,
            "users_count": users_count,
            "total_duration": total_duration,
            "user_lesson_dict": user_lesson_dict,
            'completed_lessons_count': completed_lessons_count,
        })

        return context


class UserCourseDetailsView(CourseRegistrationRequiredMixin, UserCourseTopicsView):
    model = Course
    context_object_name = 'courses'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course_id = self.kwargs.get('id')
        completed_lessons_count = get_completed_lessons_count(
            self.request.user, course_id)
        user_lesson_dict = get_user_lesson_dict(self.request.user)
        print(check_course_registration(self.request, course_id))
        context.update({
            "user_lesson_dict": user_lesson_dict,
            'completed_lessons_count': completed_lessons_count,
        })

        return context


class UserLessonView(CourseRegistrationRequiredMixin, UserCourseTopicsView):
    model = Lesson
    context_object_name = 'lessons'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course_id = self.kwargs.get('id')
        course_topic_id = self.kwargs.get('course_topic_id')
        lesson_id = self.kwargs.get('lesson_id')
        lesson = Lesson.objects.get(pk=lesson_id)
        exercise = Exercise.objects.get(
            lesson=lesson_id,
            course=course_id)
        user_course_topic_quizzes = get_user_course_topic_quizzes(
            self.request.user,
            course_id,
            course_topic_id)
        completed_lessons_count = get_completed_lessons_count(
            self.request.user, course_id)
        user_lesson_dict = get_user_lesson_dict(self.request.user)

        if self.request.user.is_authenticated:
            user_exercise = UserExercises.objects.filter(
                user=self.request.user, exercise=exercise).first()

        # Add more data to the context specific to this view
        context.update({
            "lesson": lesson,
            "lesson_id": lesson_id,
            "user_exercise": user_exercise,
            "course_topic_id": course_topic_id,
            "user_lesson_dict": user_lesson_dict,
            'completed_lessons_count': completed_lessons_count,
            'user_course_topic_quizzes': user_course_topic_quizzes
        })

        return context


class UserExerciseView(CourseRegistrationRequiredMixin, UserCourseTopicsView):
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
        user_course_topic_quizzes = get_user_course_topic_quizzes(
            self.request.user,
            course_id,
            course_topic_id)

        completed_lessons_count = get_completed_lessons_count(
            self.request.user, course_id)
        user_lesson_dict = get_user_lesson_dict(self.request.user)

        if self.request.user.is_authenticated:
            user_exercise = UserExercises.objects.filter(
                user=self.request.user, exercise=exercise).first()

        # Add more data to the context specific to this view
        context.update({
            "lesson": lesson,
            "exercise": exercise,
            "lesson_id": lesson_id,
            "user_exercise": user_exercise,
            "course_topic_id": course_topic_id,
            "user_lesson_dict": user_lesson_dict,
            'completed_lessons_count': completed_lessons_count,
            'user_course_topic_quizzes': user_course_topic_quizzes
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
                    "❌ Incorrect solution, go through the lesson again and comeback to solve the exercise!",
                    extra_tags='alert alert-danger alert-dismissible fade show')

                # TODO: check if solution is correct, if yes, mark lesson and exercise for user as completed
                # and save users solution
            elif exercise.answer == solution_output:

                user_lesson, lesson_created = create_user_lesson(
                    user=request.user,
                    lesson=exercise.lesson,
                    progress=100,
                    completed=True
                )

                user_exercise, exercise_created = create_user_exercise(
                    user=request.user,
                    exercise=exercise,
                    solution=solution,
                    progress=100,
                    completed=True
                )

                if lesson_created and exercise_created:
                    messages.success(
                        request,
                        " ✅ Correct solution, you move on to the next exercise!",
                        extra_tags='alert alert-success alert-dismissible fade show')

            return redirect(redirect_url)

        messages.error(
            request, "Please solve the exercise before submission!",
            extra_tags='alert alert-danger alert-dismissible fade show')
        self.get_context_data(form=lesson_exercise_form)

        return redirect(redirect_url)


class UserCourseTopicQuizzesView(CourseRegistrationRequiredMixin, UserCourseTopicsView):
    model = CourseTopicQuiz
    context_object_name = 'course_topic_quizzes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course_id = self.kwargs.get('id')
        course_topic_id = self.kwargs.get('course_topic_id')
        lesson_id = self.kwargs.get('lesson_id')
        lesson = Lesson.objects.get(pk=lesson_id)
        course_topic = CourseTopic.objects.get(pk=course_topic_id)
        user_course_topic_quizzes = get_user_course_topic_quizzes(
            self.request.user,
            course_id,
            course_topic_id)
        exercise = Exercise.objects.get(
            lesson=lesson_id,
            course=course_id)

        completed_lessons_count = get_completed_lessons_count(
            self.request.user, course_id)
        user_lesson_dict = get_user_lesson_dict(self.request.user)

        if self.request.user.is_authenticated:
            user_exercise = UserExercises.objects.filter(
                user=self.request.user, exercise=exercise).first()

        # Add more data to the context specific to this view
        context.update({
            "lesson": lesson,
            "exercise": exercise,
            "lesson_id": lesson_id,
            "course_topic": course_topic,
            "user_exercise": user_exercise,
            "course_topic_id": course_topic_id,
            "user_lesson_dict": user_lesson_dict,
            'completed_lessons_count': completed_lessons_count,
            'user_course_topic_quizzes': user_course_topic_quizzes
        })

        return context


class SubmitUserCourseTopicQuizzesView(UserCourseTopicsView):
    def post(self, request, *args, **kwargs):

        try:
            data = json.loads(request.body)
            # print(data)
        except json.JSONDecodeError:
            return JsonResponse({"status": "error", "message": "Invalid JSON format"}, status=400)

        # Add all required keys here
        required_keys = ["course_topic_id", "course_id"]
        missing_keys = [key for key in required_keys if key not in {
            list(item.keys())[0] for item in data}]

        if missing_keys:
            return JsonResponse({"status": "error", "message": f"Missing parameters: {', '.join(missing_keys)}"}, status=400)

        try:
            keys_to_remove = {'csrfmiddlewaretoken',
                              'course_topic_id', 'course_id'}
            filtered_data = []
            for item in data:
                filtered_item = {key: value for key,
                                 value in item.items() if key not in keys_to_remove}
                if filtered_item:
                    filtered_data.append(filtered_item)

            course_topic_quiz_ids = [list(item.keys())[0]
                                     for item in filtered_data]
            course_topic_quizzes = CourseTopicQuiz.objects.filter(
                pk__in=course_topic_quiz_ids)

            course_topic_quiz_dict = {
                quiz.pk: quiz for quiz in course_topic_quizzes}

            # Process and save data to the database
            user = request.user
            user_course_topic_quizzes = []
            for item in filtered_data:
                key = list(item.keys())[0]
                value = item[key]
                course_topic_quiz = course_topic_quiz_dict.get(int(key))

                if value == course_topic_quiz.correct_answer:
                    score = 1
                else:
                    score = 0

                user_course_topic_quiz = UserCourseTopicQuizzes(
                    user=user,
                    score=score,
                    answer=value,
                    completed=True,
                    course_topic_quiz=course_topic_quiz,
                )
                user_course_topic_quizzes.append(user_course_topic_quiz)
                # print(f"Saving {key}: {value}")
            print(course_topic_quiz_ids)
            if user_course_topic_quizzes:
                with transaction.atomic():  # Ensure atomicity
                    UserCourseTopicQuizzes.objects.filter(
                        course_topic_quiz_id__in=course_topic_quiz_ids
                    ).delete()
                    UserCourseTopicQuizzes.objects.bulk_create(
                        user_course_topic_quizzes)

            return JsonResponse({"status": "success", "message": f"Quizzes successfully saved"})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=500)

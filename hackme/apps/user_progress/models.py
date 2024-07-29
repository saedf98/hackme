from django.db import models

from apps.common.models import TimeStampedModel
from apps.course_quizzes.models import CourseQuiz
from apps.course_topic_quizzes.models import CourseTopicQuiz
from apps.course_topics.models import CourseTopic
from apps.courses.models import Course
from apps.exercises.models import Exercise
from apps.lesson_quizzes.models import LessonQuiz
from apps.lessons.models import Lesson
from apps.users.models import User


# Create your models here.
# TODO(toheeb): move this if it is not best here
class UserCourses(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.RESTRICT)
    progress = models.IntegerField(default=0)
    completed = models.BooleanField(default=False)

    class Meta:
        db_table = 'user_courses'


class UserCourseTopics(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course_topic = models.ForeignKey(CourseTopic, on_delete=models.RESTRICT)
    progress = models.IntegerField(default=0)
    completed = models.BooleanField(default=False)

    class Meta:
        db_table = 'user_course_topics'

    def __str__(self):
        return f"{self.user.username} - {self.course_topic.title}"


class UserLessons(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.RESTRICT)
    progress = models.IntegerField(default=0)
    completed = models.BooleanField(default=False)

    class Meta:
        db_table = 'user_lessons'

    def __str__(self):
        return f"{self.user.username} - {self.lesson.title}"


class UserExercises(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.RESTRICT)
    solution = models.TextField()
    progress = models.IntegerField(default=0)
    completed = models.BooleanField(default=False)

    class Meta:
        db_table = 'user_exercises'


class UserCourseQuizzes(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course_quiz = models.ForeignKey(CourseQuiz, on_delete=models.RESTRICT)
    answer = models.CharField(max_length=100)
    score = models.IntegerField(default=0)
    completed = models.BooleanField(default=False)

    class Meta:
        db_table = 'user_course_quizzes'


class UserCourseTopicQuizzes(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course_topic_quiz = models.ForeignKey(
        CourseTopicQuiz, on_delete=models.RESTRICT)
    answer = models.CharField(max_length=100)
    score = models.IntegerField(default=0)
    completed = models.BooleanField(default=False)

    class Meta:
        db_table = 'user_course_topic_quizzes'


class UserLessonQuizzes(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.CharField(max_length=100)
    lesson_quiz = models.ForeignKey(LessonQuiz, on_delete=models.RESTRICT)
    score = models.IntegerField(default=0)
    completed = models.BooleanField(default=False)

    class Meta:
        db_table = 'user_lesson_quizzes'

from django.db import models

from apps.common.models import Quiz
from apps.course_topics.models import CourseTopic
from apps.courses.models import Course
from apps.lessons.models import Lesson


# Create your models here.
class LessonQuiz(Quiz):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    course_topic = models.ForeignKey(CourseTopic, on_delete=models.CASCADE)

    class Meta:
        db_table = 'lesson_quizzes'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Quiz_detail", kwargs={"pk": self.pk})

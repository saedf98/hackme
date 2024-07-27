from django.db import models

from apps.common.models import Quiz
from apps.courses.models import Course


# Create your models here.
class CourseQuiz(Quiz):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        db_table = 'course_quizzes'

    def get_default_name(self):
        return f"{self.course.name} Quiz"

    def __str__(self):
        return self.name

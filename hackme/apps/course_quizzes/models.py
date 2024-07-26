from django.db import models

from apps.common.models import Quiz
from apps.courses.models import Course


# Create your models here.
class CourseQuiz(Quiz):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        db_table = 'course_quizzes'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("CourseQuiz_detail", kwargs={"pk": self.pk})

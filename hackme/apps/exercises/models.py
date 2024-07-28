from django.db import models

from apps.common.models import TimeStampedModel
from apps.courses.models import Course
from apps.lessons.models import Lesson


# Create your models here.
class Exercise(TimeStampedModel):
    name = models.CharField(max_length=255)
    question = models.TextField()
    answer = models.TextField()
    lesson = models.OneToOneField(Lesson, on_delete=models.RESTRICT)
    course = models.ForeignKey(Course, on_delete=models.RESTRICT)

    class Meta:
        db_table = 'exercises'

    def __str__(self):
        return self.name

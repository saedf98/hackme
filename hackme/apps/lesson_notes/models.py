from django.db import models

from apps.common.models import TimeStampedModel
from apps.lessons.models import Lesson


# Create your models here.
class LessonNote(TimeStampedModel):
    note = models.TextField()
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    class Meta:
        db_table = 'lesson_notes'

    def __str__(self):
        return self.lesson.name

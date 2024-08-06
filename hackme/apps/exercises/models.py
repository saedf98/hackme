from django.db import models
from django.utils.text import slugify
from apps.common.models import TimeStampedModel
from apps.courses.models import Course
from apps.lessons.models import Lesson


# Create your models here.
class Exercise(TimeStampedModel):
    name = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(blank=True, null=True)
    question = models.TextField()
    answer = models.TextField()
    lesson = models.OneToOneField(
        Lesson, related_name='exercise', on_delete=models.RESTRICT)
    course = models.ForeignKey(
        Course, related_name='exercises', on_delete=models.RESTRICT)

    class Meta:
        db_table = 'exercises'

    def __str__(self):
        return self.name

    def get_default_name(self):
        return f"{self.lesson.name} Exercise"

    def save(self, *args, **kwargs):
        if not self.name:
            self.name = self.get_default_name()
        if not self.slug:
            self.slug = slugify(self.get_default_name())
        super(Exercise, self).save(*args, **kwargs)

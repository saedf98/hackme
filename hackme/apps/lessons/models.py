from django.db import models
from django.utils.text import slugify
from apps.common.models import LessonFormat, TimeStampedModel
from apps.courses.models import Course


# Create your models here.
class Lesson(TimeStampedModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(blank=True, null=True)
    lesson_format = models.CharField(
        max_length=15,
        choices=LessonFormat.choices,
        default=LessonFormat.TEXT,
    )
    lesson_material = models.FileField(null=True, blank=True)
    lesson_text = models.TextField(null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.RESTRICT)

    class Meta:
        db_table = 'lessons'

    def clean(self):
        if not self.lesson_material and not self.lesson_text:
            raise ValidationError(
                "At least one of lesson_material or lesson_text must be provided.")

        # Don't forget to call the super clean method
        super().clean()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Lesson, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

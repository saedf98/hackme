from django.db import models
from django.forms import ValidationError
from django.utils.text import slugify
from apps.common.utils import estimate_reading_time, is_youtube_url
from apps.common.models import LessonFormat, TimeStampedModel
from apps.courses.models import Course
from apps.course_topics.models import CourseTopic


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
    lesson_video_link = models.CharField(max_length=400, null=True, blank=True)
    course = models.ForeignKey(
        Course,
        related_name='lessons',
        on_delete=models.RESTRICT)
    duration = models.PositiveIntegerField(blank=True)
    course_topic = models.ForeignKey(
        CourseTopic,
        related_name='lessons',
        on_delete=models.CASCADE)

    class Meta:
        db_table = 'lessons'

    def clean(self):
        if not self.lesson_material and not self.lesson_text:
            raise ValidationError(
                "At least one of Lesson material or Lesson text must be provided.")

        if self.lesson_format == LessonFormat.TEXT:
            if not self.lesson_text:
                raise ValidationError(
                    "Please input the lesson text.")
            self.duration = estimate_reading_time(self.lesson_text)

        elif self.lesson_format in (LessonFormat.VIDEO, LessonFormat.PDF):
            if not self.lesson_material:
                raise ValidationError(
                    "Please upload lesson material.")

        elif self.lesson_format == LessonFormat.VIDEO_LINK:
            if not self.lesson_video_link:
                raise ValidationError(
                    "Please input lesson video link (youtube only allowed).")

            if not is_youtube_url(self.lesson_video_link):
                raise ValidationError(
                    "Only youtube links are allowed.")

        else:
            if not self.lesson_material:
                raise ValidationError(
                    "Please upload lesson material.")

            if not self.lesson_text:
                raise ValidationError(
                    "Please input the lesson text.")

        if self.duration is None:
            raise ValidationError(
                "Please enter the duration of the video or complete material.")
            # Don't forget to call the super clean method

        super().clean()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        if self.lesson_format == LessonFormat.TEXT:
            self.duration = estimate_reading_time(self.lesson_text)
        super(Lesson, self).save(*args, **kwargs)

    @property
    def has_exercise(self):
        print("I got here")
        return self.exercise.exists()

    def __str__(self):
        return self.name

from django.db import models
from django.utils.text import slugify
from apps.common.models import TimeStampedModel
from apps.courses.models import Course


# Create your models here.
class CourseTopic(TimeStampedModel):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(blank=True, null=True)
    description = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.RESTRICT)

    class Meta:
        db_table = 'course_topics'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(CourseTopic, self).save(*args, **kwargs)

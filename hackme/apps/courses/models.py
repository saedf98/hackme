from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from apps.common.models import TimeStampedModel, CourseFormat
from apps.levels.models import Level


# Create your models here.
class Course(TimeStampedModel):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='course_images')
    course_format = models.CharField(
        max_length=15,
        choices=CourseFormat.choices,
        default=CourseFormat.TEXT,
    )
    level = models.ForeignKey(
        Level,
        on_delete=models.RESTRICT
    )
    content_type = models.ForeignKey(ContentType, on_delete=models.RESTRICT)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        db_table = 'courses'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Course_detail", kwargs={"pk": self.pk})

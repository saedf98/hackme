from django.db import models

from apps.common.models import TimeStampedModel
from apps.courses.models import Course


# Create your models here.
class CourseTopic(TimeStampedModel):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.RESTRICT)

    class Meta:
        db_table = 'course_topics'

    def get_absolute_url(self):
        return reverse("CourseTopic_detail", kwargs={"pk": self.pk})

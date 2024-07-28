from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from apps.common.models import TimeStampedModel
from apps.courses.models import Course


# Create your models here.
class DigitalForensic(TimeStampedModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=False, null=False)
    hash_type = models.CharField(max_length=255)
    courses = GenericRelation(Course)

    class Meta:
        db_table = 'digital_forensics'

    def __str__(self):
        return self.name

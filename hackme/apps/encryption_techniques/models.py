from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from apps.common.models import TimeStampedModel, EncryptionType
from apps.courses.models import Course

# Create your models here.


class EncryptionTechnique(TimeStampedModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=False, null=False)
    encryption_type = models.CharField(
        max_length=10,
        choices=EncryptionType.choices,
        default=EncryptionType.SYMMETRIC,
    )
    courses = GenericRelation(Course)

    class Meta:
        db_table = 'encryption_techniques'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("EncryptionTechnique_detail", kwargs={"pk": self.pk})

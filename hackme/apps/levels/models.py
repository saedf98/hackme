from django.db import models

from apps.common.models import TimeStampedModel


# Create your models here.
class Level(TimeStampedModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        db_table = 'levels'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Level_detail", kwargs={"pk": self.pk})

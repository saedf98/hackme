from django.db import models
from django.utils.text import slugify
from apps.common.models import TimeStampedModel


# Create your models here.
class Level(TimeStampedModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(blank=True, null=True)

    class Meta:
        db_table = 'levels'

    def save(self, *args, **kwargs):
        if not self.slug or self.slug != slugify(self.name):
            self.slug = slugify(self.name)
        super(Level, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

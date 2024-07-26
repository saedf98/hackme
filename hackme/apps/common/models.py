from django.db import models
from django.utils.translation import gettext as _


# Create your models here.
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Quiz(TimeStampedModel):
    name = models.CharField(max_length=255)
    question = models.TextField()
    options = models.JSONField(blank=False, null=False)
    correct_answer = models.CharField(max_length=255)

    class Meta:
        abstract = True


class CourseFormat(models.TextChoices):
    TEXT = "text", _("Text")
    VIDEO = "video", _("Video")
    TEXT_VIDEO = "text_and_video", _("Text And Video")


class LessonFormat(models.TextChoices):
    TEXT = "text", _("Text")
    VIDEO = "video", _("Video")
    PDF = "pdf", _("PDF")
    TEXT_VIDEO = "text_and_video", _("Text And Video")


class EncryptionType(models.TextChoices):
    SYMMETRIC = 'symmetric', _('Symmetric')
    ASYMMETRIC = 'asymmetric', _('Asymmetric')

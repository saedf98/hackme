from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext as _


# Create your models here.
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Quiz(TimeStampedModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(blank=True, null=True)
    question = models.TextField()
    options = models.JSONField(blank=False, null=False)
    correct_answer = models.CharField(max_length=255)

    class Meta:
        abstract = True

    def get_default_name(self):
        # Child classes should override this method to provide specific logic
        # return "Default Quiz Name"
        raise NotImplementedError(
            "Subclasses must implement get_default_name method")

    def save(self, *args, **kwargs):
        if not self.name:
            self.name = self.get_default_name()
        if not self.slug:
            self.slug = slugify(self.get_default_name())
        super(Quiz, self).save(*args, **kwargs)


class CourseFormat(models.TextChoices):
    TEXT = "text", _("Text")
    VIDEO = "video", _("Video")
    TEXT_VIDEO = "text_and_video", _("Text And Video")


class CourseStatus(models.TextChoices):
    DRAFT = 'draft', _("Draft")
    PUBLISHED = 'published', _("Published")
    ARCHIVED = 'archived', _("Archived")


class LessonFormat(models.TextChoices):
    TEXT = "text", _("Text")
    VIDEO = "video", _("Video")
    PDF = "pdf", _("PDF")
    TEXT_VIDEO = "text_and_video", _("Text And Video")
    VIDEO_LINK = "video_link", _("Video Link")


class EncryptionType(models.TextChoices):
    SYMMETRIC = 'symmetric', _('Symmetric')
    ASYMMETRIC = 'asymmetric', _('Asymmetric')

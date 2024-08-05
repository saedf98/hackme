from django.db import models
from django.utils.text import slugify
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from apps.common.models import TimeStampedModel, CourseFormat, CourseStatus
from apps.levels.models import Level
from apps.users.models import User


# Create your models here.
class Course(TimeStampedModel):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(blank=True, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to='course_images')
    course_format = models.CharField(
        max_length=15,
        choices=CourseFormat.choices,
        default=CourseFormat.TEXT,
    )
    course_status = models.CharField(
        max_length=15,
        choices=CourseStatus.choices,
        default=CourseStatus.DRAFT,
    )
    level = models.ForeignKey(
        Level,
        on_delete=models.RESTRICT
    )
    instructor = models.ForeignKey(User, on_delete=models.RESTRICT)
    content_type = models.ForeignKey(ContentType, on_delete=models.RESTRICT, limit_choices_to={
        # Replace with actual app labels
        'app_label__in': ['encryption_techniques', 'hashing_algorithms', 'digital_forensics'],
        # Replace with actual model names
        'model__in': ['encryptiontechnique', 'hashingalgorithm', 'digitalforensic'],
    })
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        db_table = 'courses'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        if not self.object_id and self.content_type:
            # Set the object_id to a specific ID based on some logic
            self.object_id = self.get_default_object_id()
            print(self.object_id)
        super(Course, self).save(*args, **kwargs)

    def get_default_object_id(self):
        model_class = self.content_type.model_class()
        first_object = model_class.objects.first()
        return first_object.id if first_object else None

    def __str__(self):
        return self.name

    def get_content_object(self):
        if self.content_type and self.object_id:
            model_class = self.content_type.model_class()
            return model_class.objects.get(id=self.object_id)
        return None

import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    pass

    class Meta:
        db_table = 'users'


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, related_name='profile', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=True)
    verification_token = models.UUIDField(default=uuid.uuid4, editable=False)
    email_verified = models.BooleanField(default=False)
    profile_picture = models.ImageField(
        upload_to='profile_pictures',
        blank=True, null=True)

    class Meta:
        db_table = 'user_profile'

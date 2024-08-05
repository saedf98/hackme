import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    pass

    class Meta:
        db_table = 'users'


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=True)
    verification_token = models.UUIDField(default=uuid.uuid4, editable=False)
    email_verified = models.BooleanField(default=False)

    class Meta:
        db_table = 'user_profile'

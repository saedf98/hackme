from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from apps.users.models import User, UserProfile
from .mails import send_verification_email


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = UserProfile.objects.create(user=instance)
        user_profile.username = instance.username
        user_profile.email = instance.email
        send_verification_email(user_profile)


@receiver(post_save, sender=UserProfile)
def send_verification_on_update(sender, instance, **kwargs):
    if not instance.email_verified:
        user = User.objects.get(id=instance.user_id)
        user.verification_token = instance.verification_token
        send_verification_email(user)

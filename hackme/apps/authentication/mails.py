from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.urls import reverse


def send_verification_email(user):
    subject = 'Email Verification'
    to_email = user.email

    # Construct the verification link
    base_url = settings.BASE_URL
    token_path = reverse("auth:verify_email", args=[user.verification_token])
    verification_link = f'{base_url}{token_path}'

    # Render the HTML template with context data
    html_content = render_to_string('emails/email_verification.html', {
        'user': user,
        'verification_link': verification_link,
        'app_name': settings.APP_NAME
    })

    # Create a plain text version for fallback
    text_content = strip_tags(html_content)

    # Create the email
    email = EmailMultiAlternatives(
        subject, text_content, settings.DEFAULT_FROM_EMAIL, [to_email])
    email.attach_alternative(html_content, "text/html")

    # Send the email
    email.send()

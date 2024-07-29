from django.urls import path
from .views import LoginAuthView, RegisterAuthView, ForgetPasswordAuthView, AuthView, ResentEmailVerificationView

app_name = "auth"

urlpatterns = [
    path(
        "auth/login/",
        LoginAuthView.as_view(template_name="auth_login_basic.html"),
        name="login",
    ),
    path(
        "auth/register/",
        RegisterAuthView.as_view(template_name="auth_register_basic.html"),
        name="register",
    ),
    path(
        "auth/forgot_password/",
        ForgetPasswordAuthView.as_view(
            template_name="auth_forgot_password_basic.html"),
        name="forgot-password",
    ),
    path(
        'verify/<uuid:token>/',
        AuthView.verify_email,
        name='verify_email'
    ),
    path(
        'auth/resend_email_verification/',
        ResentEmailVerificationView.as_view(
            template_name="auth_resend_email_verification.html"),
        name='resend_email_verification'
    ),

    # TODO(toheeb): fix logout
    path(
        "auth/logout/",
        AuthView.logout_user,
        name="logout",
    ),
]

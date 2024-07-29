import uuid
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect
from web_project import TemplateLayout
from apps.common.utils import get_url
from django.views.generic import TemplateView
from apps.users.models import User, UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from web_project.template_helpers.theme import TemplateHelper


"""
This file is a view controller for multiple pages as a module.
Here you can override the page view layout.
Refer to auth/urls.py file for more pages.
"""


class AuthView(TemplateView):
    # Predefined function
    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))

        # Update the context
        context.update({
            "layout_path": TemplateHelper.set_layout("layout_blank.html", context),
        })

        return context

    def verify_email(request, token):
        try:
            profile = UserProfile.objects.get(verification_token=token)
            profile.email_verified = True
            profile.save()
            messages.success(
                request, 'Email Verified Successfully.',
                extra_tags='alert alert-success alert-dismissible fade show')
        except UserProfile.DoesNotExist:
            messages.error(
                request, 'Invalid verification, please try again.',
                extra_tags='alert alert-danger alert-dismissible fade show')

        return redirect(reverse("auth:login"))

    @login_required()
    def logout_user(self, request):
        logout(request)
        return redirect('home')


class LoginAuthView(AuthView):

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.userprofile.email_verified:
                login(request, user)
                # redirect_url = request.GET.get('next', 'home')
                redirect_url = request.GET.get('next', 'index')
            else:
                messages.error(request, f"Please verify your account <a href='{get_url('auth:resend_email_verification')}'>click here</a> !",
                               extra_tags='alert alert-danger alert-dismissible fade show')
                redirect_url = reverse("auth:login")
        else:
            messages.error(request, "Username Or Password is incorrect!",
                           extra_tags='alert alert-danger alert-dismissible fade show')
            redirect_url = reverse("auth:login")

        return redirect(redirect_url)
        # return HttpResponse("I am here")


class RegisterAuthView(AuthView):
    def post(self, request, *args, **kwargs):
        check1 = False
        check2 = False
        check3 = False
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password_confirmation')
        email = request.POST.get('email')

        if password != password2:
            check1 = True
            messages.error(request, 'Password did not match!',
                           extra_tags='alert alert-danger alert-dismissible fade show')
        if User.objects.filter(username=username).exists():
            check2 = True
            messages.error(request, 'Username already exists!',
                           extra_tags='alert alert-danger alert-dismissible fade show')
        if User.objects.filter(email=email).exists():
            check3 = True
            messages.error(request, 'Email already registered!',
                           extra_tags='alert alert-danger alert-dismissible fade show')

        if check1 or check2 or check3:
            messages.error(
                request, "Registration Failed!", extra_tags='alert alert-danger alert-dismissible fade show')
            redirect_url = redirect('auth:register')
        else:
            user = User.objects.create_user(
                username=username, password=password, email=email)
            messages.success(
                request, f'Thanks for registering {user.username}, Please check your mail inbox to verify your account.', extra_tags='alert alert-success alert-dismissible fade show')
            redirect_url = redirect('auth:login')

        return redirect(redirect_url)


class ResentEmailVerificationView(AuthView):
    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')

        try:
            user = User.objects.get(email=email)
            if not user.userprofile.email_verified:
                user.userprofile.verification_token = uuid.uuid4()  # Generate a new token
                user.userprofile.save()
                messages.success(
                    request, 'Verification email has been resent.', extra_tags='alert alert-success alert-dismissible fade show')
            else:
                messages.info(request, 'This email is already verified.',
                              extra_tags='alert alert-info alert-dismissible fade show')
        except User.DoesNotExist:
            messages.error(request, 'Please enter a valid email.',
                           extra_tags='alert alert-danger alert-dismissible fade show')

        return redirect(reverse("auth:resend_email_verification"))


class ForgetPasswordAuthView(AuthView):
    def post(self, request, *args, **kwargs):

        # form = self.form_class(data=request.POST)
        return HttpResponse("I am here")

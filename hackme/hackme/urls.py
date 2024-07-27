"""
URL configuration for hackme project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from web_project.views import SystemView

# TODO(toheeb): update all underscores to hyphen

urlpatterns = [
    path('admin/', admin.site.urls),

    # Levels urls
    path("", include("apps.levels.urls")),

    # Lessons url
    path("", include("apps.lessons.urls")),

    # Courses urls
    path("", include("apps.courses.urls")),

    # Course Quizzes
    path("", include("apps.course_quizzes.urls")),

    # Course topics url
    path("", include("apps.course_topics.urls")),

    # Course topics quizzes url
    path("", include("apps.course_topic_quizzes.urls")),

    # Lesson quizzes url
    # Lesson notes url
    # Exercise url
    # Digital Forensics url
    # Encryption Techniques url
    # Hashing Algorithms url

    # Dashboard urls
    path("", include("apps.dashboards.urls")),

    # layouts urls
    path("", include("apps.layouts.urls")),

    # Pages urls
    path("", include("apps.pages.urls")),

    # Auth urls
    path("", include("apps.authentication.urls")),

    # Card urls
    path("", include("apps.cards.urls")),

    # UI urls
    path("", include("apps.ui.urls")),

    # Extended UI urls
    path("", include("apps.extended_ui.urls")),

    # Icons urls
    path("", include("apps.icons.urls")),

    # Forms urls
    path("", include("apps.forms.urls")),

    # FormLayouts urls
    path("", include("apps.form_layouts.urls")),

    # Tables urls
    path("", include("apps.tables.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = SystemView.as_view(
    template_name="pages_misc_error.html", status=404)
handler400 = SystemView.as_view(
    template_name="pages_misc_error.html", status=400)
handler500 = SystemView.as_view(
    template_name="pages_misc_error.html", status=500)

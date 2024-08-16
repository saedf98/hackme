from django.urls import path
from .views import DashboardsView, LandingPageView


urlpatterns = [
    path(
        "",
        LandingPageView.as_view(template_name="landing_page.html"),
        name="index",
    ),
    path(
        "dashboard",
        DashboardsView.as_view(template_name="dashboard_analytics.html"),
        name="dashboard",
    )
]

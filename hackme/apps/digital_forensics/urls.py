from django.urls import path
from .views import DigitalForensicView

app_name = "digital_forensics"

urlpatterns = [
    path(
        "digital_forensics/",
        DigitalForensicView.as_view(
            template_name="digital_forensics/index.html"),
        name="index",
    ),
    path(
        "digital_forensics/create/",
        DigitalForensicView.as_view(
            template_name="digital_forensics/create.html"),
        name="create",
    ),
    path(
        "digital_forensics/edit/<int:id>/",
        DigitalForensicView.as_view(
            template_name="digital_forensics/edit.html"),
        name="edit",
    ),
    path(
        "digital_forensics/show/<int:id>/",
        DigitalForensicView.as_view(
            template_name="digital_forensics/show.html"),
        name="show",
    ),
]

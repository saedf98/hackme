from django.urls import path
from .views import EncryptionTechniqueView

app_name = "encryption_techniques"

urlpatterns = [
    path(
        "encryption_techniques/",
        EncryptionTechniqueView.as_view(
            template_name="encryption_techniques/index.html"),
        name="index",
    ),
    path(
        "encryption_techniques/create/",
        EncryptionTechniqueView.as_view(
            template_name="encryption_techniques/create.html"),
        name="create",
    ),
    path(
        "encryption_techniques/edit/<int:id>/",
        EncryptionTechniqueView.as_view(
            template_name="encryption_techniques/edit.html"),
        name="edit",
    ),
    path(
        "encryption_techniques/show/<int:id>/",
        EncryptionTechniqueView.as_view(
            template_name="encryption_techniques/show.html"),
        name="show",
    ),
]

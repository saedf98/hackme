from django.urls import path
from .views import HashingAlgorithmView

app_name = "hashing_algorithms"

urlpatterns = [
    path(
        "hashing_algorithms/",
        HashingAlgorithmView.as_view(
            template_name="hashing_algorithms/index.html"),
        name="index",
    ),
    path(
        "hashing_algorithms/create/",
        HashingAlgorithmView.as_view(
            template_name="hashing_algorithms/create.html"),
        name="create",
    ),
    path(
        "hashing_algorithms/edit/<int:id>/",
        HashingAlgorithmView.as_view(
            template_name="hashing_algorithms/edit.html"),
        name="edit",
    ),
    path(
        "hashing_algorithms/show/<int:id>/",
        HashingAlgorithmView.as_view(
            template_name="hashing_algorithms/show.html"),
        name="show",
    ),
]

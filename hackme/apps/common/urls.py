from django.urls import path
from .editor import EditorView, EditorRunCodeView

app_name = "common"

urlpatterns = [
    path('run-code/', EditorRunCodeView.as_view(), name='run_code'),
    path(
        "online-editor/",
        EditorView.as_view(
            template_name="common/editor.html"),
        name="editor",
    ),
]

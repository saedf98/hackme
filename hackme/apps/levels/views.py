from django.urls import reverse_lazy
from apps.common.views import DahsboardView
from .models import Level
from .tables import LevelTable


# Create your views here.
class LevelView(DahsboardView, LevelTable):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        levels = LevelTable()
        # table = LevelTable(data=Level.objects.all())
        # Add more data to the context specific to this view
        context.update({
            "additional_data": "This is some additional data for MyView",
            "levels": levels,
            # Example of adding a URL to the context
            "some_url": reverse_lazy('some_named_url'),
        })

        return context

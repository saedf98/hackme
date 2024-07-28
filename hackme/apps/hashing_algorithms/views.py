from django.urls import reverse_lazy
from apps.common.views import DashboardView
from .models import HashingAlgorithm
from .tables import HashingAlgorithmTable


# Create your views here.
class HashingAlgorithmView(DashboardView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        hashing_algorithms = HashingAlgorithmTable()
        # table = HashingAlgorithmTable(data=HashingAlgorithmView.objects.all())
        # Add more data to the context specific to this view
        context.update({
            "additional_data": "This is some additional data for MyView",
            "hashing_algorithms": hashing_algorithms,
            # Example of adding a URL to the context
            "some_url": reverse_lazy('some_named_url'),
        })

        return context

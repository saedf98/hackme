from django.urls import reverse_lazy
from apps.common.views import DashboardView
from .models import EncryptionTechnique
from .tables import EncryptionTechniqueTable


# Create your views here.
class EncryptionTechniqueView(DashboardView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        encryption_techniques = EncryptionTechniqueTable()
        # table = EncryptionTechniqueTable(data=EncryptionTechnique.objects.all())
        # Add more data to the context specific to this view
        context.update({
            "additional_data": "This is some additional data for MyView",
            "encryption_techniques": encryption_techniques,
            # Example of adding a URL to the context
            "some_url": reverse_lazy('some_named_url'),
        })

        return context

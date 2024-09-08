from django.urls import reverse_lazy
# from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
from apps.common.views import DashboardView
# from apps.common.utils import in_user_group
from .models import User
from .tables import UserTable


# Create your views here.
class UserView(DashboardView, UserTable):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        users = UserTable()
        # table = UserTable(data=User.objects.all())
        # Add more data to the context specific to this view
        context.update({
            "additional_data": "This is some additional data for MyView",
            "users": users,
            # Example of adding a URL to the context
            "some_url": reverse_lazy('some_named_url'),
        })

        return context


class UserShowView(DashboardView):
    model = User

    def get(self, request, id, *args, **kwargs):
        user = get_object_or_404(User, id=id)
        context = self.get_context_data()
        context.update({
            "curr_user": user,
            "curr_user_role": user.groups.all()[0].name
        })
        return self.render_to_response(context)

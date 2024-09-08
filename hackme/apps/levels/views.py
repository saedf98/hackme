from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from apps.common.views import DashboardView
from apps.common.utils import get_config_value
from .models import Level
from .tables import LevelTable
from .forms import LevelForm


# Create your views here.
class LevelView(DashboardView, LevelTable):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        levels = LevelTable()
        # table = LevelTable(data=Level.objects.all())
        # Add more data to the context specific to this view
        context.update({
            "levels": levels,
            # Example of adding a URL to the context
            "some_url": reverse_lazy('some_named_url'),
        })

        return context


class LevelCreateView(DashboardView, CreateView):
    model = Level
    form_class = LevelForm

    def get(self, request, *args, **kwargs):
        self.object = None
        # self.object_list = self.get_queryset()
        context = self.get_context_data()
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        # Associate the level with the logged-in user
        form.instance.user = self.request.user
        level = form.save()  # Save the form and create the Level instance
        redirect_url = self.request.META.get(
            'HTTP_REFERER', '/')  # Redirect to the previous page
        messages.success(
            self.request, get_config_value('common.created'),
            extra_tags='alert alert-success alert-dismissible fade show')
        return redirect(redirect_url)

    def form_invalid(self, form):
        context = self.get_context_data(form=form)
        messages.error(
            self.request, get_config_value('common.form_invalid'),
            extra_tags='alert alert-danger alert-dismissible fade show')
        return self.render_to_response(context)


class LevelShowView(DashboardView):
    model = Level

    def get(self, request, id, *args, **kwargs):
        level = get_object_or_404(Level, id=id)
        context = self.get_context_data()
        context.update({
            "level": level
        })
        return self.render_to_response(context)


class LevelUpdateView(DashboardView, UpdateView):
    model = Level
    form_class = LevelForm

    def get(self, request, id, *args, **kwargs):
        self.object = get_object_or_404(Level, id=id)
        context = self.get_context_data()
        return self.render_to_response(context)

    def post(self, request, id, *args, **kwargs):
        self.object = get_object_or_404(Level, id=id)
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.user = self.request.user
        self.object = form.save()  # Save the form and create the Level instance
        redirect_url = self.request.META.get(
            'HTTP_REFERER', '/')  # Redirect to the previous page
        messages.success(self.request, get_config_value('common.saved'),
                         extra_tags='alert alert-success alert-dismissible fade show')
        return redirect(redirect_url)

    def form_invalid(self, form):
        context = self.get_context_data(form=form)
        messages.error(
            self.request, get_config_value('common.form_invalid'),
            extra_tags='alert alert-danger alert-dismissible fade show')
        return self.render_to_response(context)


class LevelDeleteView(DeleteView):
    model = Level

    def get(self, request, id, *args, **kwargs):
        level = Level.objects.filter(id=id).first()
        redirect_url = self.request.META.get(
            'HTTP_REFERER', '/')
        if level:
            try:
                level.delete()
                messages.success(
                    self.request, get_config_value('common.removed'))
                return redirect(redirect_url)
            except Exception as e:
                messages.error(
                    self.request, f"❌ {e}!",
                    extra_tags='alert alert-danger alert-dismissible fade show')
                return redirect(redirect_url)
        else:
            messages.error(
                self.request, get_config_value('common.no_items_found'),
                extra_tags='alert alert-danger alert-dismissible fade show')
            return redirect(redirect_url)

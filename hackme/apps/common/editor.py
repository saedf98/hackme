import os
import json
import subprocess
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views import View
from apps.common.mixins import GroupRequiredMixin
from .views import BlankView
from web_project import TemplateLayout
from django.contrib.auth.mixins import LoginRequiredMixin


class EditorView(LoginRequiredMixin, GroupRequiredMixin, BlankView):
    login_url = reverse_lazy('auth:login')
    groups = ['instructor', 'admin', 'user']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        context['user'] = self.request.user
        context['user_role'] = self.request.user.groups.all()[0].name

        return context


class EditorRunCodeView(View):
    def get(self, request, *args, **kwargs) -> JsonResponse:
        return JsonResponse({'output': 'Invalid request'}, status=400)

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        language = data['language']
        code = data['code']

        if language == 'python':
            file_extension = 'py'
        elif language == 'javascript':
            file_extension = 'js'
        else:
            return JsonResponse({'output': 'Unsupported language'}, status=400)

        filename = f'code.{file_extension}'

        with open(filename, 'w') as file:
            file.write(code)

        try:
            if language == 'python':
                output = subprocess.check_output(
                    ['python', filename], stderr=subprocess.STDOUT, timeout=10)
            elif language == 'javascript':
                output = subprocess.check_output(
                    ['node', filename], stderr=subprocess.STDOUT, timeout=10)

            output = output.decode('utf-8')
        except subprocess.CalledProcessError as e:
            output = e.output.decode('utf-8')
        except Exception as e:
            output = str(e)
        finally:
            if os.path.exists(filename):
                os.remove(filename)

        return JsonResponse({'output': output})

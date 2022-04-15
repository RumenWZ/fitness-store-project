from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import UserPassesTestMixin

# Create your views here.
from django.template import loader
from django.views import generic as views
from django.views.defaults import page_not_found

from FitnessStore.main.models import Sales


class HomeView(views.TemplateView):
    template_name = 'main/index.html'


class AdminFunctionsView(UserPassesTestMixin, views.TemplateView):
    template_name = 'main/admin_functions.html'

    def test_func(self):
        result = self.request.user.is_superuser or self.request.user.is_staff
        return result


def error400(request, exception):
    return render(request, "errors/400.html", status=403)


def error403(request, exception):
    return render(request, "errors/403.html", status=403)


# def error404(request, *args, **kwargs):
#     content = loader.render_to_string('errors/404.html', {}, request)
#     return HttpResponseNotFound(content)
def error404(request):
    return render(request, 'errors/404.html')


def internal_server_error(request):
    return render(request, "errors/500.html", status=500)

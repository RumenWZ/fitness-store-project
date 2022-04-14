from django.shortcuts import render, redirect
from django.contrib.auth.mixins import UserPassesTestMixin

# Create your views here.
from django.views import generic as views

from FitnessStore.main.models import Sales


class HomeView(views.TemplateView):
    template_name = 'main/index.html'


class AdminFunctionsView(UserPassesTestMixin, views.TemplateView):
    template_name = 'main/admin_functions.html'

    def test_func(self):
        result = self.request.user.is_superuser or self.request.user.is_staff
        return result


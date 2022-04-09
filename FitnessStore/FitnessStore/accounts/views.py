from django.contrib.auth import views as auth_views
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic as views

from FitnessStore.main.forms import CreateProfileForm


class LoginProfileView(auth_views.LoginView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('index')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()

class RegisterProfileView(views.CreateView):
    template_name = 'accounts/register.html'
    form_class = CreateProfileForm
    success_url = reverse_lazy('index')
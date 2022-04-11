from django.contrib.auth import views as auth_views, authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic as views

from FitnessStore.accounts.models import Profile
# from FitnessStore.main.decorators import unauthenticated_user
from FitnessStore.main.forms import CreateProfileForm



# @unauthenticated_user
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

    # def form_valid(self, form):
    #     form.save()
    #     username = self.request.POST['username']
    #     password = self.request.POST['password1']
    #     user = authenticate(username=username, password=password)
    #     login(self.request, user)
    #     return HttpResponseRedirect(self.get_success_url)


class ProfileLogoutView(auth_views.LogoutView):
    pass


class ProfileDetailsView(views.ListView):
    model = Profile
    template_name = 'accounts/profile_details.html'
    context_object_name = 'profile'

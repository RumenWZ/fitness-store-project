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
from FitnessStore.main.models import Sales
from FitnessStore.products.models import Protein


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



class ProfileLogoutView(auth_views.LogoutView):
    pass


class ProfileDetailsView(views.ListView):
    model = Profile
    template_name = 'accounts/profile_details.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        purchases = list(Sales.objects.filter(buyer_id=self.request.user.id))
        all_proteins = Protein.objects.all()
        print(f'purchases {purchases}')
        purchase_results = []
        for purchase in purchases:
            item = list(Protein.objects.filter(product_id=purchase.product_id))
            print(item)
            purchase_results.append(item[0])
        print(purchase_results)

        print(f'All proteins: {all_proteins}')
        print(purchases)
        print(f'purch results {purchase_results}')

        context.update({
            'purchases': purchase_results,
            'x': purchases
        })

        return context
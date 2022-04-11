from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render
import json
from rest_framework.decorators import api_view



# Create your views here.
from django.urls import reverse_lazy
from django.views import generic as views

from FitnessStore.main.models import Sales
from FitnessStore.products.models import Protein


class ProteinsListView(views.ListView):
    model = Protein
    template_name = 'products/proteins_list.html'
    context_object_name = 'proteins'


# @login_required
class ProteinAddView(LoginRequiredMixin, views.CreateView):
    model = Protein
    template_name = 'products/protein_add.html'
    fields = ('name', 'picture', 'description', 'price', 'flavour',)
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProteinDetailsView(views.DetailView):
    model = Protein
    template_name = 'products/protein_details.html'
    context_object_name = 'protein'


class ProteinConfirmPurchaseView(views.DetailView):
    model = Protein
    template_name = 'products/protein_confirm.html'
    context_object_name = 'protein'


@api_view(['POST'])
def purchase_success(request):
    product_id = request.data['productId']

    customer = request.user.id
    if request.method == "POST":
        sale = Sales(buyer_id=customer, product_id=product_id)
        sale.save()

    return JsonResponse('Purchase successful', safe=False)

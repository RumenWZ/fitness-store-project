from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.http import JsonResponse
from django.shortcuts import render
import json
from rest_framework.decorators import api_view

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic as views

from FitnessStore.common.validators import check_superuser
from FitnessStore.main.forms import EditProteinForm, EditClothingForm
from FitnessStore.main.models import Sales
from FitnessStore.products.models import Protein, Clothing


class ProteinsListView(views.ListView):
    model = Protein
    template_name = 'products/proteins_list.html'
    context_object_name = 'proteins'


class ProteinAddView(UserPassesTestMixin, views.CreateView):
    model = Protein
    template_name = 'products/protein_add.html'
    fields = ('name', 'picture', 'description', 'price', 'flavour',)
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        result = self.request.user.is_superuser or self.request.user.is_staff
        return result


class ProteinDetailsView(views.DetailView):
    model = Protein
    template_name = 'products/protein_details.html'
    context_object_name = 'protein'


class ProteinConfirmPurchaseView(views.DetailView):
    model = Protein
    template_name = 'products/protein_confirm.html'
    context_object_name = 'protein'


class ProteinEditView(UserPassesTestMixin, views.UpdateView):
    model = Protein
    form_class = EditProteinForm
    template_name = 'products/protein_edit.html'
    success_url = reverse_lazy('protein list')

    def test_func(self):
        result = self.request.user.is_superuser or self.request.user.is_staff
        return result


# *******************CLOTHING***********************

class ClothingListView(views.ListView):
    model = Clothing
    template_name = 'products/clothing_list.html'
    context_object_name = 'clothing'


class ClothingAddView(UserPassesTestMixin, views.CreateView):
    model = Clothing
    template_name = 'products/clothing_add.html'
    fields = ('name', 'picture', 'description', 'price', 'size')
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        result = self.request.user.is_superuser or self.request.user.is_staff
        return result


class ClothingDetailsView(views.DetailView):
    model = Clothing
    template_name = 'products/clothing_details.html'
    context_object_name = 'clothing'


class ClothingEditView(UserPassesTestMixin, views.UpdateView):
    model = Clothing
    form_class = EditClothingForm
    template_name = 'products/clothing_edit.html'
    success_url = reverse_lazy('clothing list')

    def test_func(self):
        result = self.request.user.is_superuser or self.request.user.is_staff
        return result


class ClothingConfirmPurchaseView(views.DetailView):
    model = Clothing
    template_name = 'products/clothing_confirm.html'
    context_object_name = 'clothing'


class SuccessView(views.TemplateView):
    template_name = 'products/success.html'


@api_view(['POST'])
def purchase_success(request):
    product_id = request.data['productId']
    itemtype = request.data['action']

    print(product_id, itemtype)

    customer = request.user.id
    if request.method == "POST":
        if itemtype == "clothing":
            sale = Sales(buyer_id=customer, product_id=product_id)
            sale.save()
        elif itemtype == "protein":
            sale = Sales(buyer_id=customer, product_id=product_id)
            sale.save()

    return JsonResponse('Purchase successful', safe=False)

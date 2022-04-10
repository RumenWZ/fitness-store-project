from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic as views


from FitnessStore.products.models import Protein


class ProteinsListView(views.ListView):
    model = Protein
    template_name = 'products/proteins_list.html'
    context_object_name = 'proteins'


class ProteinAddView(views.CreateView):
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
from django.shortcuts import render

# Create your views here.
from django.views import generic as views


class ProteinsListView(views.TemplateView):
    template_name = 'main/proteins_list.html'
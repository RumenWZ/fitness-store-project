from django.shortcuts import render

# Create your views here.
from django.views import generic as views


class HomeView(views.TemplateView):
    template_name = 'main/index.html'



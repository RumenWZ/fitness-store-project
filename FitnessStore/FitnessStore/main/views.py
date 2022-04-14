from django.shortcuts import render

# Create your views here.
from django.views import generic as views

from FitnessStore.main.models import Sales


class HomeView(views.ListView):
    template_name = 'main/index.html'
    model = Sales
    context_object_name = "sales"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        total_sales = Sales.objects.all()
        print(total_sales[:3])
        context.update({
            'top_sales': total_sales[:3],
        })
        return context



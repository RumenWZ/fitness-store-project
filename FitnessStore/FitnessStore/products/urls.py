from django.urls import path

from FitnessStore.products.views import ProteinsListView

urlpatterns = (
    path('', ProteinsListView.as_view(), name='protein list'),
)
from django.urls import path

from FitnessStore.products.views import ProteinsListView, ProteinAddView, ProteinDetailsView

urlpatterns = (
    path('', ProteinsListView.as_view(), name='protein list'),
    # PROTEINS
    path('protein/add/', ProteinAddView.as_view(), name='protein add'),
    path('protein/<int:pk>', ProteinDetailsView.as_view(), name='protein details'),
    #CLOTHING

    #DRINKS

)
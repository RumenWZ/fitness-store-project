from django.urls import path

from FitnessStore.products.views import ProteinsListView, ProteinAddView, ProteinDetailsView, \
    ProteinConfirmPurchaseView, purchase_success

urlpatterns = (
    path('', ProteinsListView.as_view(), name='protein list'),
    path('success/', purchase_success, name='purchase success'),
    # PROTEINS
    path('protein/add/', ProteinAddView.as_view(), name='protein add'),
    path('protein/<str:pk>/', ProteinDetailsView.as_view(), name='protein details'),
    path('protein/confirm/<str:pk>/', ProteinConfirmPurchaseView.as_view(), name='protein confirm'),
    #CLOTHING

    #DRINKS

)
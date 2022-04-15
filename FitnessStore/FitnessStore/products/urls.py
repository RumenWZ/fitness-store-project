from django.urls import path

from FitnessStore.products.views import ProteinsListView, ProteinAddView, ProteinDetailsView, \
    ProteinConfirmPurchaseView, purchase_success, ProteinEditView, SuccessView, ClothingListView, ClothingAddView, \
    ClothingDetailsView, ClothingConfirmPurchaseView, ClothingEditView, ProteinDeleteView, ClothingDeleteView

urlpatterns = (
    path('success/', purchase_success, name='purchase success'),
    path('purchased/', SuccessView.as_view(), name='success'),
    # PROTEINS
    path('protein/', ProteinsListView.as_view(), name='protein list'),
    path('protein/add/', ProteinAddView.as_view(), name='protein add'),
    path('protein/<str:pk>/', ProteinDetailsView.as_view(), name='protein details'),
    path('protein/confirm/<str:pk>/', ProteinConfirmPurchaseView.as_view(), name='protein confirm'),
    path('protein/edit/<str:pk>/', ProteinEditView.as_view(), name='protein edit'),
    path('protien/delete/<str:pk>', ProteinDeleteView.as_view(), name='protein delete'),

    #CLOTHING
    path('clothing/',ClothingListView.as_view(), name='clothing list'),
    path('clothing/add', ClothingAddView.as_view(), name='clothing add'),
    path('clothing/<str:pk>/', ClothingDetailsView.as_view(), name='clothing details'),
    path('clothing/confirm/<str:pk>/', ClothingConfirmPurchaseView.as_view(), name='clothing confirm'),
    path('clothing/edit/<str:pk>/', ClothingEditView.as_view(), name='clothing edit'),
    path('clothing/delete/<str:pk>', ClothingDeleteView.as_view(), name='clothing delete'),
)
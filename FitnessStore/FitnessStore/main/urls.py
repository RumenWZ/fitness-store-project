from django.urls import path

from FitnessStore.main.views import HomeView, AdminFunctionsView

urlpatterns = (
    path('', HomeView.as_view(), name='index'),
    path('admin-functions/', AdminFunctionsView.as_view(), name='admin functions'),
)
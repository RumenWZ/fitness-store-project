from django.urls import path

from FitnessStore.main.views import HomeView

urlpatterns = (
    path('', HomeView.as_view(), name='index'),
)
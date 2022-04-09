from django.urls import path

from FitnessStore.accounts.views import LoginProfileView, RegisterProfileView

urlpatterns = (
    path('login/', LoginProfileView.as_view(), name='login'),
    path('register/', RegisterProfileView.as_view(), name='register')
)
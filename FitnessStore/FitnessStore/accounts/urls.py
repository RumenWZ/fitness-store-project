from django.urls import path

from FitnessStore.accounts.views import LoginProfileView, RegisterProfileView, ProfileDetailsView, ProfileLogoutView, \
    ChangePasswordView

urlpatterns = (
    path('login/', LoginProfileView.as_view(), name='login'),
    path('register/', RegisterProfileView.as_view(), name='register'),

    path('profile/', ProfileDetailsView.as_view(), name='profile details'),
    path('profile/logout/', ProfileLogoutView.as_view(), name='profile logout'),
    path('change-password/', ChangePasswordView.as_view(), name='change password'),
)
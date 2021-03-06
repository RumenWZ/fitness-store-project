from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('FitnessStore.main.urls')),
    path('products/', include('FitnessStore.products.urls')),
    path('account/', include('FitnessStore.accounts.urls')),
]

handler400 = 'FitnessStore.main.views.error400'
handler403 = 'FitnessStore.main.views.error403'

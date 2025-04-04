from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CryptocurrencyViewSet

router = DefaultRouter()

# Removing the automatic creation of the root path
router.include_root_view = False

router.register(r'cryptocurrencies', CryptocurrencyViewSet, basename='cryptocurrency')

urlpatterns = [
    path('', include(router.urls)),
]

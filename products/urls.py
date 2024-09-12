from django.urls import path
from .views import ProductTariffPromotionView

urlpatterns = [
    path('products/xml/', ProductTariffPromotionView.as_view(), name='product-tariff-promotion-xml'),
]
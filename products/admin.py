from django.contrib import admin
from .models import Product, Tariff, Promotion


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name']
    search_fields = ['product_name']


@admin.register(Tariff)
class TariffAdmin(admin.ModelAdmin):
    list_display = ['tariff_name', 'product', 'price']
    search_fields = ['tariff_name']


@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ['promotion_name', 'discount_percentage', 'date_start', 'date_end']
    list_filter = ['date_start', 'date_end']
    search_fields = ['promotion_name']
    filter_horizontal = ['tariffs']

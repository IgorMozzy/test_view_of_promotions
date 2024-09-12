from django.utils import timezone
from rest_framework import serializers
from .models import Product, Tariff


class TariffSerializer(serializers.ModelSerializer):
    promotion = serializers.SerializerMethodField()
    # https://www.django-rest-framework.org/api-guide/fields/#serializermethodfield
    base_price = serializers.CharField(source='price')
    class Meta:
        model = Tariff
        fields = ['tariff_name', 'base_price', 'promotion']

    def get_promotion(self, tariff):
        current_date = timezone.now().date()
        best_promotion = tariff.promotions.filter(date_start__lte=current_date, date_end__gte=current_date).first()
        if best_promotion:
            discounted_price = round(tariff.price * (1 - best_promotion.discount_percentage / 100), 2)
            return {
                'promotion_name': best_promotion.promotion_name,
                'discount_percentage': best_promotion.discount_percentage,
                'date_end': best_promotion.date_end,
                'discounted_price': discounted_price,
            }
        return None


class ProductSerializer(serializers.ModelSerializer):
    tariffs = TariffSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['product_name', 'tariffs']

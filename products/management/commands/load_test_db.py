# https://docs.djangoproject.com/en/5.1/howto/custom-management-commands/
# python manage.py load_test_db

from django.core.management.base import BaseCommand
from products.models import Product, Tariff, Promotion

class Command(BaseCommand):
    help = 'Loading...'

    def handle(self, *args, **kwargs):
        product1 = Product.objects.create(product_name="Product 1")
        product2 = Product.objects.create(product_name="Product 2")

        tariff1 = Tariff.objects.create(tariff_name="Tariff 1", price=1000, product=product1)
        tariff2 = Tariff.objects.create(tariff_name="Tariff 1_1", price=2000, product=product1)
        tariff3 = Tariff.objects.create(tariff_name="Tariff 2", price=3000, product=product2)

        promotion1 = Promotion.objects.create(
            promotion_name="Promotion 1",
            discount_percentage=50,
            date_start="2024-09-12",
            date_end="2024-12-31"
        )
        promotion1.tariffs.add(tariff1, tariff2)

        promotion2 = Promotion.objects.create(
            promotion_name="Promotion 2",
            discount_percentage=20,
            date_start="2024-01-01",
            date_end="2024-12-31"
        )
        promotion2.tariffs.add(tariff1, tariff2, tariff3)

        self.stdout.write(self.style.SUCCESS('Done!'))
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=250)

    def __str__(self):
        return self.product_name


class Tariff(models.Model):
    tariff_name = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='tariffs')

    def __str__(self):
        return self.tariff_name


class Promotion(models.Model):
    promotion_name = models.CharField(max_length=250)
    discount_percentage = models.DecimalField(
        validators=[MinValueValidator(0), MaxValueValidator(100)], max_digits=5, decimal_places=2)
    date_start = models.DateField()
    date_end = models.DateField()
    tariffs = models.ManyToManyField(Tariff, blank=True, related_name='promotions')


    class Meta:
        ordering = ['-discount_percentage']

    # https://docs.djangoproject.com/en/5.1/ref/models/instances/#django.db.models.Model.clean
    def clean(self):
        if self.date_start > self.date_end:
            raise ValidationError('The end date MUST be after start date!')

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.promotion_name

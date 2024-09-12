from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_xml.renderers import XMLRenderer
from .models import Product
from .serializers import ProductSerializer

# https://www.django-rest-framework.org/api-guide/renderers/
class ProductTariffPromotionView(APIView):
    renderer_classes = [XMLRenderer]

    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

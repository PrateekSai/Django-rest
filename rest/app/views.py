from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product

@api_view(["GET"])
def get_products(request):
    products=Product.objects.all()
    serialized = ProductSerializer(products,many=True)
    return Response(serialized.data)
@api_view(["GET"])
def get_product(request,pk):
    product = get_object_or_404(Product,pk=pk)
    serialized = ProductSerializer(product)
    return Response(serialized.data)


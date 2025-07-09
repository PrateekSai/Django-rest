from rest_framework import serializers
from .models import Product
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['pk','name', 'description', 'price', 'stock']

    def valid_price(self,value):
        if value<=0:
            raise serializers.ValidationError("price should be greater than 0")
        return value

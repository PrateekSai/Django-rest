from django.contrib import admin
from .models import Product,OrderItem,Order

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
# Register your models here.

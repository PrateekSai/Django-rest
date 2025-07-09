from django.urls import path
from . import views
urlpatterns = [
    path("Products/",views.get_products,name = "products"),
    path("Product/<int:pk>/",views.get_product,name ="get_product")
    ]
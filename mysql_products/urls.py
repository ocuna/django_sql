from django.urls import path
from mysql_products.views import products

urlpatterns = [
    path('products/<slug:category>', products),
]
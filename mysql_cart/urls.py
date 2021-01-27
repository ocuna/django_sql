from django.urls import path
from mysql_cart.views import Cookie

urlpatterns = [
    path('cart/cookie/', Cookie),
    path('cart/cookie/<slug:arg>', Cookie),
]


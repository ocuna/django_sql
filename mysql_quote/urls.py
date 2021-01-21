from django.urls import path
from mysql_quote.views import displayQuote

urlpatterns = [
    path('quote/', displayQuote),
]
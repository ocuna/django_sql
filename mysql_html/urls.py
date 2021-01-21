from django.urls import path
from mysql_html.views import display, displayDateTime, home

urlpatterns = [
    path('', home),
    path('html/', display),
    path('html/dt', displayDateTime),
]
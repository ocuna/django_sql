from django.urls import path
from mysql_html.views import display, displayDateTime, home, displayEmployee

urlpatterns = [
    path('', home),
    path('html/', display),
    path('html/dt', displayDateTime),
    path('html/employee', displayEmployee),
]
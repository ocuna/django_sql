from django.urls import path
from mysql_clinic.views import Clinic_LP

# ▐▓▒░ ͶΔͲΞ ░▒▓▌

urlpatterns = [
    path('clinic',Clinic_LP),
]
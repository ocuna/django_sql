from django.urls import path
from mysql_hr.views import employeeData, passengerData, passengerDelete, passengerUpdate, passengerRegistration, passengerLogin, modelPassengerRegistration

urlpatterns = [
    path('hr/employees',employeeData),
    path('hr/passengers',passengerData),
    path('hr/passenger/delete/<int:id>',passengerDelete),
    path('hr/passenger/update/<int:id>',passengerUpdate),
    path('hr/passengerRegistration',passengerRegistration),
    path('hr/modelPassengerRegistration',modelPassengerRegistration),
    path('hr/passengerLogin',passengerLogin),
]
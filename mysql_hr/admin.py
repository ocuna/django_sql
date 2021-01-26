from django.contrib import admin
from mysql_hr.models import Employee, Passenger

# another way to have the employee Admin display admin records
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['email']

admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Passenger)
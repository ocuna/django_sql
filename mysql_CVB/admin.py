from django.contrib import admin
from mysql_CVB.models import Students

# another way to have the employee Admin display admin records
class StudentsAdmin(admin.ModelAdmin):
    list_display=['email']

admin.site.register(Students,StudentsAdmin)

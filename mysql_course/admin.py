from django.contrib import admin
from mysql_course.models import Courses

# another way to have the employee Admin display admin records
class CoursesAdmin(admin.ModelAdmin):
    list_display=['name']

admin.site.register(Courses,CoursesAdmin)
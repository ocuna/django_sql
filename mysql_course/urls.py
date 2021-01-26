from django.urls import path
from mysql_course.views import courseCRUD

urlpatterns = [
    path('courses',courseCRUD),
    path('courses/delete/<int:id>',courseCRUD),
    path('courses/update/<int:id>',courseCRUD),
]
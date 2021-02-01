from django.urls import path, include
from mysql_CVB.views import GreetingView, StudentsListView, StudentsDetailView, StudentsCreateView, StudentsUpdateView, StudentsDeleteView

urlpatterns = [
    path('cbv', GreetingView.as_view(greetingMessage='Howdie Partner ... it\'s still CVB Land!')),
    path('cbv/students/', StudentsListView.as_view(), name="studentList"),
    path('cbv/stundents/logout', GreetingView.as_view(greetingMessage='Bye!')),
    path('cbv/students/create', StudentsCreateView.as_view(), name="createStudent"),
    path('cbv/students/details/<int:pk>/', StudentsDetailView.as_view(), name="studentDetails"),
    path('cbv/students/update/<int:pk>/', StudentsUpdateView.as_view(), name="studentUpdate"),
    path('cbv/students/delete/<int:pk>/', StudentsDeleteView.as_view())
]
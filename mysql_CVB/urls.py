from django.urls import path
from mysql_CVB.views import GreetingView, StudentsListView, StudentsDetailView, StudentsCreateView, StudentsUpdateView, StudentsDeleteView

urlpatterns = [
    path('cvb', GreetingView.as_view(greetingMessage='Howdie Partner ... it\'s still CVB Land!')),
    path('cvb/students/', StudentsListView.as_view(), name="studentList"),
    path('cvb/students/create', StudentsCreateView.as_view(), name="createStudent"),
    path('cvb/students/details/<int:pk>/', StudentsDetailView.as_view(), name="studentDetails"),
    path('cvb/students/update/<int:pk>/', StudentsUpdateView.as_view(), name="studentUpdate"),
    path('cvb/students/delete/<int:pk>/', StudentsDeleteView.as_view()),

]
from django.shortcuts import render
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from mysql_CVB.models import Students
from django.urls import reverse_lazy

# Create your views here.
class GreetingView(View):
    greetingMessage = 'IT\'s CVB Time!'
    def get(self,request):
        self.greetingMessage = '<div class="p-2 bg-warning text-white fw-bold">' + self.greetingMessage + '</div>'
        return HttpResponse(self.greetingMessage)

class StudentsListView(ListView):
    model = Students
    #default template_name = model_list.html - in our case: "student_list.html"
    template_name = 'studentlist.html'
    #default context_object_name = model_list - in our case: "student_list"
    context_object_name = 'students'
    #adding contextual data to the object: https://docs.djangoproject.com/en/3.1/topics/class-based-views/generic-display/
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the view
        context['heading'] = 'Student List'
        return context

class StudentsDetailView(DetailView):
    model = Students
    #default template_name = model_list.html - in our case: "student_detail.html"
    template_name = 'studentdetail.html'
    #default context_object_name = model_list - in our case: "student_detail"
    context_object_name = 'student'

    #adding contextual data to the object: https://docs.djangoproject.com/en/3.1/topics/class-based-views/generic-display/
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the view
        context['heading'] = 'Student Details'
        return context

class StudentsCreateView(CreateView):
    model = Students
    fields = ('first','last','email','grade')
    #default template_name = model_list.html - in our case: "student_list.html"
    template_name = 'studentcreate.html'
    #default context_object_name = model_list - in our case: "student_list"
    context_object_name = 'form'
    #adding contextual data to the object: https://docs.djangoproject.com/en/3.1/topics/class-based-views/generic-display/
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the view
        context['heading'] = 'Create Student'
        return context

class StudentsUpdateView(UpdateView):
    model = Students
    fields = ('email','grade')
    #default template_name = model_list.html - in our case: "student_list.html"
    template_name = 'studentcreate.html'
    #default context_object_name = model_list - in our case: "student_list"
    context_object_name = 'student'
    #adding contextual data to the object: https://docs.djangoproject.com/en/3.1/topics/class-based-views/generic-display/
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the view
        context['heading'] = 'Update Student'
        return context

class StudentsDeleteView(DeleteView):
    model = Students
    success_url = reverse_lazy('studentList')
    fields = ('first','last')
    #default template_name = model_list.html - in our case: "student_list.html"
    template_name = 'studentConfirmDelete.html'
    #default context_object_name = model_list - in our case: "student_list"
    context_object_name = 'student'
    #adding contextual data to the object: https://docs.djangoproject.com/en/3.1/topics/class-based-views/generic-display/
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the view
        context['heading'] = 'Delete Student'
        return context

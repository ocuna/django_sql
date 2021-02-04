from django.shortcuts import render
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse

# Create your views here.
class Clinic_LP(View):
    # we must declare this attribute if the django can pass it in from urls.py
    greetingMessage = ''
    temp = '<h1>We\'re underconstruction yo!</h1>'
    def get(self,request):
        self.greetingMessage = '<div>' + self.greetingMessage + '</div>'
        return HttpResponse(str(self.temp) + self.greetingMessage)

'''
class ClinicListView(ListView):
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
'''
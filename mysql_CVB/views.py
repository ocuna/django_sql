from django.shortcuts import render
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from mysql_CVB.models import Students
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from mysql.decorators import group_required

# Create your views here.
class GreetingView(View):
    # we must declare this attribute if the django can pass it in from urls.py
    greetingMessage = ''
    temp = '<h1>IT\'s CVB Time!</h1><p><a href="/accounts/login?next=/cbv/students/">Login</a> if you got it...'
    def get(self,request):
        self.greetingMessage = '<div>' + self.greetingMessage + '</div>'
        return HttpResponse(str(self.temp) + self.greetingMessage)

# decorator is going to modify each view through "decorating wrapping"
@method_decorator(login_required, name="dispatch")
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

@method_decorator(login_required, name="dispatch")
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

@method_decorator(login_required, name="dispatch")
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

@method_decorator(login_required, name="dispatch")
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

# https://stackoverflow.com/questions/36177769/django-groups-and-permissions
# https://stackoverflow.com/questions/29673549/method-decorator-with-login-required-and-permission-required
# the user must be POWERUSER to access this CBV
decorators = [login_required,group_required(u"poweruser")] 
@method_decorator(decorators, name="dispatch")
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

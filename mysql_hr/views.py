from django.shortcuts import render, redirect
from mysql_hr.models import Employee, Passenger
from mysql_hr import forms

# Create your views here.
def employeeData(request):
    employees = Employee.objects.all()
    context = {
        'heading':"Employees",
        'employees':employees,
    }
    return render(request, 'employees.html', context)

def passengerDelete(request,id):
    passenger = Passenger.objects.get(id=id)
    passenger.delete()
    return redirect('/hr/passengers')

def passengerData(request):
    passengers = Passenger.objects.all()
    context = {
        'heading':"Passengers",
        'passengers':passengers,
    }
    return render(request, 'passengers.html', context)

# this is essentially the same thing as passengerCreate - but we are passing the instance the passenger object
def passengerUpdate(request,id):
    passenger = Passenger.objects.get(id=id)
            # if the form is filled out correctly go to the Passengers page
    if request.method == 'POST':
        # this very cool function pre-fills the form with the instance POST and passenger (because not everything may have changed in the update)
        form = forms.modelPassengerRegistration(request.POST, instance=passenger)
        if form.is_valid():
            form.save()
            return redirect('/hr/passengers')
    else:
        # this very cool function fills the form with initial record that's pulled above
        form = forms.modelPassengerRegistration(initial=passenger.__dict__)

    context = {
        'heading':"Model-Based Passenger Update",
        'form': form,
    }

    return render(request, 'modelPassengerRegistration.html', context)


def modelPassengerRegistration(request):
    successString = ''
    POST = ''
    if request.method == 'POST':
        form = forms.modelPassengerRegistration(request.POST)
        POST = request.POST
        if form.is_valid():
            form.save()
            return redirect('/hr/passengers')
    else :
        form = forms.modelPassengerRegistration

    context = {
        'heading':"Model-Based Passenger Registration",
        'form':form,
        'POST': POST,
        'success': successString
    }
    return render(request, 'modelPassengerRegistration.html', context)

def passengerRegistration(request):
    successString = ''
    POST = ''
    if request.method == 'POST':
        form = forms.passengerRegistration(request.POST)
        POST = request.POST
        if form.is_valid():
            successString = form.cleaned_data['first'] + " " + form.cleaned_data['last'] + " has been registered with email: " + form.cleaned_data['email']
    else :
        form = forms.passengerRegistration

    context = {
        'heading':"Passenger Registration",
        'form':form,
        'successString': successString,
        'POST': POST,
    }
    return render(request, 'passengerRegistration.html', context)

   
def passengerLogin(request):
    successString = ''
    POST = ''
    if request.method == 'POST':
        form = forms.passengerLogin(request.POST)
        POST = request.POST
        if form.is_valid():
            successString = "Login successful for User Name (email): " + form.cleaned_data['email'] + " | Password: " + form.cleaned_data['password']
    else :
        form = forms.passengerLogin

    context = {
        'heading':"Passenger Login",
        'form':form,
        'successString': successString,
        'POST': POST,
    }
    return render(request, 'passengerLogin.html', context)
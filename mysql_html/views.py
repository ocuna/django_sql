from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
# function based view:
def home(request):
    #http reponse simply sends back HTML -- very basic
    return HttpResponse('<a href="/quote/">quote</a><br><a href="/html/dt">DateTime</a><br><a href="/html/">Greeting</a><br>')

def display(request):
    return HttpResponse("<h1>This is MySQL_HTML Application</h1>")

def displayDateTime(request):
    dt=datetime.datetime.now()
    #string
    s='<b>Curent Date and Time: </b>' + str(dt)
    #the object HttpResponse is necessary to wrap whatever response is going back from the server to the browser
    return HttpResponse(s)
from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
# function based view:
def home(request):
    # http reponse simply sends back HTML -- very basic
    # return HttpResponse('<a href="/quote/">quote</a><br><a href="/html/dt">DateTime</a><br><a href="/html/">Greeting</a><br>')
    context = {
        'html': '<a href="/quote/">quote</a><br><a href="/html/dt">DateTime</a><br><a href="/html/">Greeting</a><br>'
    }
    return render(request,'base.html', context)

def display(request):
    context = {
        'html': '<h1>This is MySQL_HTML Application</h1>'
    }
    return render(request,'base.html', context)

def displayDateTime(request):
    dt=datetime.datetime.now()
    #s = string
    s='<b>Curent Date and Time: </b>' + str(dt)
    context = {
        'html': s
    }
    return render(request,'base.html', context)
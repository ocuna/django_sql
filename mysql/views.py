from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# function based view:
def nope_403(request):
    # http reponse simply sends back HTML -- very basic
    # return HttpResponse('<a href="/quote/">quote</a><br><a href="/html/dt">DateTime</a><br><a href="/html/">Greeting</a><br>')
    context = {
        'html': 'You don\'t have access to this function.  Contact the adminstrator.'
    }
    return render(request,'home.html', context)
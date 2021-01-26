from django.shortcuts import render
from mysql_course.models import Courses
from mysql_course.forms import coursesModelForm

def courseCRUD(request,id='1'):
    '''

    '''
    courses = Courses.objects.all()
    course = ''
    mtype = ''
    mtext = ''
    action = ''
    form = ''

    #is the user requesting the page
    if request.method == 'GET':
        if request.path.find('/delete/') != -1 :
            course = Courses.objects.get(id=id)
            action = 'create'
            course.delete()
            mtype = 'warning'
            mtext = 'It\'s your fault.  Course ' + str(course.name) + ' has been irrevocably deleted forever.'
            form = coursesModelForm

        else :
            action = 'create'
            form = coursesModelForm

    #is the user posting changes?
    elif request.method == 'POST':
        if 'update' in request.POST:
            course = Courses.objects.get(id=id)
            form = coursesModelForm(request.POST, instance=course)
            if form.is_valid():
                form.save()
                mtype = 'info'
                mmessage = 'You have successfully updated course: ' + str(course.name) + '.'
            else:
                mtype = 'info'
                mmessage = 'An error in submission occured, please check your information and try again.'
                # this very cool function fills the form with initial record that's pulled above
                form = coursesModelForm(initial=course.__dict__)

        elif 'create' in request.POST:
            if form.is_valid():
                form.save()
                mtype = 'success'
                mmessage = 'Great! The new course: ' + str(course.name) + ' has been created.'
                form = forms.courses

    message = {'type': mtype, 'text': mtext}
    context = {
        'courses': courses,
        'message': message,
        'heading': 'Courses: View, Create, Update and Delete',
        'form' : form,
        'action' : action,
    }
    return render(request, 'courses.html', context)

from django.shortcuts import render
from mysql_course.models import Courses
from mysql_course.forms import coursesModelForm

def courseCRUD(request,id=None):
    courses = Courses.objects.all()
    course = ''
    mtype = ''
    mtext = ''
    action = ''
    form = ''
    POST = ''

    #is the user requesting the page
    if request.method == 'GET':
        if request.path.find('/delete/') != -1 :
            course = Courses.objects.get(id=id)
            course.delete()
            action = 'create'
            mtype = 'warning'
            mtext = 'You are responsible for  irrevocably deleting the course: ' + str(course.name) + '.'
            form = coursesModelForm

        if request.path.find('/update/') != -1 :
            course = Courses.objects.get(id=id)
            action = 'update'
            form = coursesModelForm(initial=course.__dict__)

        else :
            action = 'create'
            form = coursesModelForm

    #is the user posting changes?
    elif request.method == 'POST':
        # POST = request.POST['name']
        if 'update' in request.POST:
            course = Courses.objects.get(id=id)
            form = coursesModelForm(request.POST, instance=course)
            if form.is_valid():
                form.save()
                mtype = 'info'
                mtext = 'You have successfully updated course: ' + str(course.name) + '.'
                action = 'create'
                form = coursesModelForm
            else:
                action = 'update'
                form = coursesModelForm(request.POST, instance=course)

        elif 'create' in request.POST:
            form = coursesModelForm(request.POST)
            if form.is_valid():
                form.save()
                mtype = 'success'
                mtext = 'Great! The new course: ' + str(request.POST['name']) + ' has been created.'
                action = 'create'
                form = coursesModelForm

    message = {'type': mtype, 'text': mtext}
    context = {
        'courses': courses,
        'message': message,
        'heading': 'Courses: View, Create, Update and Delete',
        'form' : form,
        'action' : action,
        'POST' : POST,
    }
    return render(request, 'courses.html', context)

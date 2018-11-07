from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from gitpub.logging import debug
from .models import Course

# GET /courses
@debug
def index(request):
    courses = Course.objects.all()
    courses = sorted(courses, key=lambda x: x.id)
    return render(request, 'courses/index.html', {'courses': courses})

# GET /courses/1
@debug
def show(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'courses/show.html', {'course': course})

# GET /courses/new
@debug
def new(request):
    return render(request, 'courses/new.html')

# POST /courses/create
@debug
def create(request):
    Course.objects.create(
        name=request.POST['course_name'],
        description=request.POST['course_description']
    )
    return redirect('/courses')

# GET /courses/edit/1
@debug
def edit(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'courses/edit.html', {'course': course})

# POST /courses/edit/1/update
@debug
def update(request):
    course = get_object_or_404(Course, id=request.POST['course_id'])
    course.name = request.POST['course_name']
    course.description = request.POST['course_description']
    course.save()
    redirect_url = "/courses/" + str(course.id) + "/"
    return redirect(redirect_url)

# GET /courses/delete/1
@debug
def delete(request):
    pass
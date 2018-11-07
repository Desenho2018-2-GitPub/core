from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from gitpub.logging import debug
from .models import Course

# GET /courses
@debug
def index(request):
    courses = Course.objects.all()
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

# PATCH/PUT /courses/edit/1
@debug
def edit(request):
    pass

# DELETE /courses/1
@debug
def delete(request):
    pass
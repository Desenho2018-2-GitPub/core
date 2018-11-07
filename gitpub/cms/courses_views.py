from django.shortcuts import render
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
def show(request):
    pass

# GET /courses/new
@debug
def new(request):
    pass

# POST /courses
@debug
def create(request):
    pass

# PATCH/PUT /courses/1
@debug
def edit(request):
    pass

# DELETE /courses/1
@debug
def delete(request):
    pass
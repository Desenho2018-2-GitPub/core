from django.shortcuts import render
from django.http import HttpResponse
from gitpub.logging import debug
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseNotFound

from .models import Course, Classroom

@debug
def index(request):
    return render(request, 'index.html')

@debug
def login(request):
    return render(request, 'authentication/login.html')

@debug
def register(request):
    return render(request, 'authentication/register.html')

@debug
def forgot_password(request):
    return render(request, 'authentication/forgot-password.html')

@debug
def classrooms(request, course_id):
    try:
        Course.objects.get(pk=course_id)
    except ObjectDoesNotExist as error:
        # return HttpResponseNotFound()
        pass
    data = { 'course_id': course_id }
    return render(request, 'classrooms/classrooms.html', data)

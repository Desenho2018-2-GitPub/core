from django.shortcuts import render
from django.http import HttpResponse
from gitpub.logging import debug
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseNotFound

from cms.models import Course, Classroom

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
    return render(request, 'authentication/forgot_password.html')

@debug
def dashboard(request):
    courses = Course.objects.all()
    courses = sorted(courses, key=lambda x: x.id)
    return render(request, 'dashboard.html', {'courses': courses})

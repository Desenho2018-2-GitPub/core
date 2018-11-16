from django.shortcuts import render
from django.http import HttpResponse
from gitpub.logging import debug
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseNotFound
from django.contrib import auth
from django.shortcuts import redirect

from cms.models import Course, Classroom

@debug
def index(request):
    return render(request, 'index.html')

@debug
def login(request):
    if not request.user.is_authenticated:
        return render(request, 'authentication/login.html')
    else:
        return redirect('/dashboard')

@debug
def authenticate(request):
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(request, username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return redirect('/dashboard')
    else:
        return redirect('/login')

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

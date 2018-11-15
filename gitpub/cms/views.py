from django.shortcuts import render
from django.http import HttpResponse
from gitpub.logging import debug

# Create your views here.
@debug
def index(request):
    return render(request, 'index.html')

@debug
def login(request):
    return render(request, 'login.html')

@debug
def register(request):
    return render(request, 'register.html')

@debug
def forgot_password(request):
    return render(request, 'forgot_password.html')
    
@debug
def dashboard(request):
    return render(request, 'dashboard.html')

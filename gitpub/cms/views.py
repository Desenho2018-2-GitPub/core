from django.shortcuts import render
from django.http import HttpResponse
from gitpub.logging import debug

# Create your views here.
@debug
def index(request):
    return render(request, 'index.html')

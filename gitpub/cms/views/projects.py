from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from gitpub.logging import debug
from cms.models import Course, Classroom
from django.contrib.auth.decorators import login_required

@debug
@login_required(login_url='/login')
def new(request, course_id, classroom_id):
    return HttpResponse("NEW")

@debug
@login_required(login_url='/login')
def create(request, course_id, classroom_id):
    pass

@debug
@login_required(login_url='/login')
def show(request, course_id, classroom_id):
    return HttpResponse("SHOW")

@debug
@login_required(login_url='/login')
def index(request, course_id, classroom_id):
    return HttpResponse("OK")

@debug
@login_required(login_url='/login')
def edit(request, course_id, classroom_id):
    return HttpResponse("EDIT")

@debug
@login_required(login_url='/login')
def update(request, course_id, classroom_id):
    pass

@debug
@login_required(login_url='/login')
def delete(request, course_id, classroom_id):
    pass
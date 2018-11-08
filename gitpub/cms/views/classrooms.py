from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from gitpub.logging import debug
from cms.models import Classroom, Course, RegisteredUser, Period
from django.core.exceptions import MultipleObjectsReturned

# GET /courses/course_id/classrooms
@debug
def index(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    classrooms = Classroom.objects.filter(course__id=course_id)
    data = {
        'classrooms': classrooms,
        'course_id': course_id
    }
    return render(request, 'classrooms/index.html', data)

# GET /courses/course_id/classrooms/classroom_id
@debug
def show(request, course_id, classroom_id):
    classroom = get_object_or_404(Classroom, id=classroom_id)
    data = {
        'classroom': classroom,
        'enrolled_users': classroom.enrolled_users.all()
    }
    return render(request, 'classrooms/show.html', data)

# GET /courses/course_id/classrooms/new
@debug
def new(request, course_id):
    data = {
        'course_id': course_id
    }
    return render(request, 'classrooms/new.html', data)

# POST /courses/course_id/classrooms/new
@debug
def create(request, course_id):
    classroom_owner, ucreated = RegisteredUser.objects.get_or_create(id=1, registry=1, username='bla', email='bla@bla.com')
    try:
        classroom_period, pcreated = Period.objects.get_or_create(
            year=request.POST['period_year'],
            semester=request.POST['period_semester']
        )
    except MultipleObjectsReturned:
        classroom_period = Period.objects.filter(
            year=request.POST['period_year'],
            semester=request.POST['period_semester']
        )[0]

    Classroom.objects.create(
        name=request.POST['classroom_name'],
        course=Course.objects.get(id=course_id),
        owner=classroom_owner,
        period=classroom_period
    )
    return redirect('/courses/' + course_id + '/classrooms')

# # GET /courses/edit/1
# @debug
# def edit(request, course_id):
#     course = get_object_or_404(Course, id=course_id)
#     return render(request, 'courses/edit.html', {'course': course})

# # POST /courses/edit/1/update
# @debug
# def update(request):
#     course = get_object_or_404(Course, id=request.POST['course_id'])
#     course.name = request.POST['course_name']
#     course.description = request.POST['course_description']
#     course.save()
#     redirect_url = "/courses/" + str(course.id) + "/"
#     return redirect(redirect_url)

# GET /courses/delete/1
@debug
def delete(request, course_id, classroom_id):
    classroom = get_object_or_404(Classroom, id=classroom_id)
    classroom.delete()
    return redirect('/courses/' + course_id + '/classrooms/')
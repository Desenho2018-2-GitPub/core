from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from gitpub.logging import debug
from cms.models import Classroom, Course

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

# # GET /courses/1
# @debug
# def show(request, course_id):
#     course = get_object_or_404(Course, id=course_id)
#     return render(request, 'courses/show.html', {'course': course})

# GET /courses/course_id/classrooms/new
@debug
def new(request):
    return render(request, 'classrooms/new.html')

# # POST /courses/course_id/classrooms/new
# @debug
# def create(request):
#     Course.objects.create(
#         name=request.POST['course_name'],
#         description=request.POST['course_description']
#     )
#     return redirect('/courses')

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

# # GET /courses/delete/1
# @debug
# def delete(request, course_id):
#     course = get_object_or_404(Course, id=course_id)
#     course.delete()
#     return redirect('/courses')
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from gitpub.logging import debug
from cms.models import Classroom, Project, Course, AnonymousUser, Comment
from django.contrib.auth.decorators import login_required


@debug
@login_required(login_url='/login')
def new(request, course_id, classroom_id):
    return render(request, 'projects/new.html',
                  {'course_id': course_id, 'classroom_id': classroom_id})


@debug
@login_required(login_url='/login')
def create(request, course_id, classroom_id):
    name = request.POST.get('name')
    description = request.POST.get('description')
    classroom = Classroom.objects.get(id=classroom_id)

    project = Project(
        name=name,
        description=description
    )

    project.observers = []  # So it does not notify nobody on next save
    project.save()

    project.classroom.set([classroom])

    # So it notifies observers
    project.observers = list(classroom.enrolled_users.all())
    project.save()

    project.observers = []

    redirect_url = '/courses/{0}/classrooms/{1}'.format(
        course_id, classroom_id)

    return redirect(redirect_url)


@debug
def show(request, course_id, classroom_id, project_id):
    project = Project.objects.get(id=project_id)
    classroom = Classroom.objects.get(id=classroom_id)
    course = Course.objects.get(id=course_id)

    project.views += 1
    project.save()

    return render(request,
                  'projects/show.html',
                  {'project': project,
                   'classroom': classroom,
                   'course': course})


@debug
@login_required(login_url='/login')
def edit(request, course_id, classroom_id, project_id):
    project = Project.objects.get(id=project_id)
    classroom = Classroom.objects.get(id=classroom_id)
    course = Course.objects.get(id=course_id)
    return render(request,
                  'projects/edit.html',
                  {'project': project,
                   'classroom': classroom,
                   'course': course})


@debug
@login_required(login_url='/login')
def update(request, course_id, classroom_id):
    project_data = {
        'name': request.POST.get('name'),
        'description': request.POST.get('description')
    }

    project = Project.objects.get(id=request.POST.get('id'))
    project.__dict__.update(**project_data)
    project.save()

    redirect_url = '/courses/{0}/classrooms/{1}/projects/{2}'.format(
        course_id, classroom_id, project.id)

    return redirect(redirect_url)


@debug
@login_required(login_url='/login')
def delete(request, course_id, classroom_id, project_id):
    project = Project.objects.get(id=project_id)
    project.delete()

    redirect_url = '/courses/{0}/classrooms/{1}/'.format(
        course_id, classroom_id)

    return redirect(redirect_url)


@debug
def comment(request, course_id, classroom_id, project_id):
    project = Project.objects.get(id=project_id)

    text = request.POST.get('comment_text')

    if request.user.is_authenticated:
        user = request.user
    else:
        user = AnonymousUser.objects.create(name='Anonymous User')

    classroom = Classroom.objects.get(id=classroom_id)

    comment = Comment(text=text, user=user, project=project)

    comment.save()

    redirect_url = '/courses/{0}/classrooms/{1}/projects/{2}'.format(
        course_id, classroom_id, project_id)

    return redirect(redirect_url)

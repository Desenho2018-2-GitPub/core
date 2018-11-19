from django.shortcuts import render
from django.http import HttpResponse
from gitpub.logging import debug
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseNotFound
from django.contrib import auth
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import signals
from django.dispatch import receiver

from cms.models import Course, Classroom


@debug
def index(request):
    return render(request, 'index.html')


@debug
def login(request):
    print(request)

    redirect_url = '/dashboard'

    if request.GET.get('next') is not None:
        redirect_url = request.GET.get('next')

    errors = request.session.get('errors', [])
    request.session['errors'] = []

    if not request.user.is_authenticated:
        return render(request,
                      'authentication/login.html',
                      {'next': redirect_url, 'errors': errors})
    else:
        return redirect(redirect_url)


def authenticate(request):
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(request, username=username, password=password)

    redirect_url = '/dashboard'

    if request.POST.get('next') is not None:
        redirect_url = request.POST.get('next')

    if user is not None:
        auth.login(request, user)
        return redirect(redirect_url)
    else:
        request.session['errors'] = [
            'Login não efetuado. Verifique suas credenciais.']

        return redirect('/login?next={0}'.format(redirect_url))


@debug
def create_user(request):
    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']
    registry = request.POST['registry']
    name = request.POST['name']

    User = auth.get_user_model()

    User.objects.create_user(
        name=name,
        username=username,
        email=email,
        registry=registry,
        password=password
    )

    user = auth.authenticate(request, username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return redirect('/dashboard')
    else:
        return redirect('/')


@debug
def logout(request):
    auth.logout(request)
    return redirect('/')


@debug
def register(request):
    return render(request, 'authentication/register.html')


@debug
def forgot_password(request):
    return render(request, 'authentication/forgot_password.html')


@debug
@login_required(login_url='/login')
def dashboard(request):
    courses = Course.objects.all()
    courses = sorted(courses, key=lambda x: x.id)
    classrooms = Classroom.objects.all()
    classrooms = sorted(classrooms, key=lambda x: x.id)
    return render(
        request, 'dashboard.html', {
            'courses': courses, 'classrooms': classrooms})


@debug
@login_required(login_url='/login')
def update_user(request):
    user_data = {
        'name': request.POST.get('name'),
        'username': request.POST.get('username'),
        'email': request.POST.get('email'),
        'registry': request.POST.get('registry'),
        'bio': request.POST.get('bio')
    }
    User = auth.get_user_model()

    user = User.objects.get(id=request.user.id)

    user.__dict__.update(**user_data)

    user.save()

    return redirect('/dashboard')

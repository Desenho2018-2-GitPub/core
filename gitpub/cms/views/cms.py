from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.http import HttpResponseNotFound
from django.contrib import auth
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import signals
from django.dispatch import receiver

from gitpub.logging import debug
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
    name = request.POST['name']
    username = request.POST['username']
    email = request.POST['email']
    registry = request.POST['registry']
    password = request.POST['password']

    redirect_url = '/dashboard'

    User = auth.get_user_model()

    try:
        User.objects.create_user(
            name=name,
            username=username,
            email=email,
            registry=registry,
            password=password)

    except IntegrityError as e:
        request.session['errors'] = [
            'Email ou usuário já cadastrado, entre com sua conta.']
        return redirect('/login?next={0}'.format(redirect_url))

    except ValueError as e:
        request.session['errors'] = [
            'Cadastro não efetuado. Verifique suas credenciais.']
        return redirect('/register?next={0}'.format(redirect_url))

    # log user
    try:
        user = auth.authenticate(request, username=username, password=password)
        auth.login(request, user)
        return redirect('/dashboard')
    except Exception as e:
        request.session['errors'] = [
            'Usuário não pode ser autenticado.']
        return redirect('/register?next={0}'.format(redirect_url))

@debug
def logout(request):
    auth.logout(request)
    return redirect('/')


@debug
def register(request):
    redirect_url = '/dashboard'

    if request.GET.get('next') is not None:
        redirect_url = request.GET.get('next')

    errors = request.session.get('errors', [])
    request.session['errors'] = []

    if not request.user.is_authenticated:
        return render(request,
                      'authentication/register.html',
                      {'next': redirect_url, 'errors': errors})
    else:
        return redirect(redirect_url)


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
    return render(request, 'dashboard.html', {'courses': courses, 'classrooms': classrooms})


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

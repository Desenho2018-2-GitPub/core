from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from gitpub.logging import debug, GitPubDebugger
from cms.models import Course

# Create your views here.
@debug
def create_course_form_get(request):
    # return HttpResponse('This is create course')
    return render(request, 'create_course_form.html')

@debug
def create_course_form_post(request):
    try:
        Course.objects.create(
            description="Test",
            name="Name"
        )
    except:
        debugger_instance = GitPubDebugger()
        debugger_instance.error("Failed to create course")
    return HttpResponseRedirect(reverse('cms:index'))
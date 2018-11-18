from django.urls import path
from cms.views import projects
from django.conf.urls import url

urlpatterns = [
    url(r'^new/$', projects.new, name='projects_new'),
    url(r'^create/$', projects.create, name='projects_create'),
    url(r'^update/$', projects.update, name='projects_update'),
    url(r'^edit/(?P<project_id>\d+)/$', projects.edit, name='projects_edit'),
    url(r'^delete/(?P<project_id>\d+)/$', projects.delete, name='projects_delete'),
    url(r'^(?P<project_id>\d+)/$', projects.show, name='projects_show'),
]

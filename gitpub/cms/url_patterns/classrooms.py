from django.urls import path
from cms.views import classrooms
from django.conf.urls import url
from cms.url_patterns import projects
from django.urls import include

urlpatterns = [
    url(r'^new/$', classrooms.new, name='classrooms_new'),
    url(r'^create/$', classrooms.create, name='classrooms_create'),
    url(r'^update/$', classrooms.update, name='classrooms_update'),
    url(r'^edit/(?P<classroom_id>\d+)/$', classrooms.edit, name='classrooms_edit'),
    url(r'^delete/(?P<classroom_id>\d+)/$', classrooms.delete, name='classrooms_delete'),
    url(r'^(?P<classroom_id>\d+)/subscribe$', classrooms.subscribe, name='classrooms_subscribe'),
    url(r'^(?P<classroom_id>\d+)/unsubscribe$', classrooms.unsubscribe, name='classrooms_unsubscribe'),
    url(r'^(?P<classroom_id>\d+)/projects/', include(projects)),
    url(r'^(?P<classroom_id>\d+)/$', classrooms.show, name='classrooms_show'),
    url(r'^$', classrooms.index, name='classrooms_index')
]

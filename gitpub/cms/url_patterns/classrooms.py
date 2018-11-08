from django.urls import path
from cms.views import classrooms
from django.conf.urls import url

urlpatterns = [
    # url(r'^new/$', classrooms.new, name='classrooms_new'),
    # url(r'^create/$', classrooms.create, name='classrooms_create'),
    # url(r'^update$', classrooms.update, name='classrooms_update'),
    # url(r'^edit/(?P<course_id>\d+)/$', classrooms.edit, name='classrooms_edit'),
    # url(r'^delete/(?P<course_id>\d+)/$', classrooms.delete, name='classrooms_delete'),
    # url(r'^(?P<course_id>\d+)/$', classrooms.show, name='classrooms_show'),
    url(r'^$', classrooms.index, name='classrooms_index')
]

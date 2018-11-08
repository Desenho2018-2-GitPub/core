from django.urls import path
from cms.views import courses
from django.conf.urls import url
from ..url_patterns import classrooms
from django.urls import include

urlpatterns = [
    url(r'^new/$', courses.new, name='courses_new'),
    url(r'^create/$', courses.create, name='courses_create'),
    url(r'^update$', courses.update, name='courses_update'),
    url(r'^edit/(?P<course_id>\d+)/$', courses.edit, name='courses_edit'),
    url(r'^delete/(?P<course_id>\d+)/$', courses.delete, name='courses_delete'),
    url(r'^(?P<course_id>\d+)/$', courses.show, name='courses_show'),
    url(r'^$', courses.index, name='courses_index'),
    url(r'^(?P<course_id>\d+)/classrooms', include(classrooms))
]

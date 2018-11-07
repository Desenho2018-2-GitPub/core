from django.urls import path
from . import views, courses_views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^courses/new/$', courses_views.new, name='courses_new'),
    url(r'^courses/create/$', courses_views.create, name='courses_create'),
    url(r'^courses/update$', courses_views.update, name='courses_update'),
    url(r'^courses/edit/(?P<course_id>\d+)/$', courses_views.edit, name='courses_edit'),
    url(r'^courses/delete/(?P<course_id>\d+)/$', courses_views.delete, name='courses_delete'),
    url(r'^courses/(?P<course_id>\d+)/$', courses_views.show, name='courses_show'),
    url(r'^courses/$', courses_views.index, name='courses_index'),
]

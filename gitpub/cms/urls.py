from django.urls import path
from . import views, courses_views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^courses/(?P<course_id>\d+)/$', courses_views.show, name='courses_show'),
    url(r'^courses/$', courses_views.index, name='courses_index'),
]

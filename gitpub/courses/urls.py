from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^new/', views.create_course_form_get, name='create_course_form_get'),
    url(r'^post_new/', views.create_course_form_post, name='create_course_form_post'),
]
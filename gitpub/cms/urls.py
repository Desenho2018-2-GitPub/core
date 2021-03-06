from django.urls import path
from .views import cms
from .url_patterns import courses
from django.conf.urls import url
from django.urls import include
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', cms.index, name='index'),
    url(r'^login', cms.login, name='login'),
    url(r'^register', cms.register, name='register'),
    url(r'^forgot_password', cms.forgot_password, name='forgot_password'),
    url(r'^dashboard', cms.dashboard, name='dashboard'),
    url(r'^authenticate', cms.authenticate, name='authenticate'),
    url(r'^logout', cms.logout, name='logout'),
    url(r'^create_user', cms.create_user, name='create_user'),
    url(r'^update_user', cms.update_user, name='update_user'),
    url(r'^courses/', include(courses))
]

from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^login', views.login, name='login'),
    url(r'^register', views.register, name='register'),
    url(r'', views.index, name='index')
]

from django.urls import path
from .views import cms
from .url_patterns import courses
from django.conf.urls import url
from django.urls import include
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from cms.core import views as core_views

urlpatterns = [
    url(r'^$', cms.index, name='index'),
    url(r'^courses/', include(courses)),
    url(r'^signup/$', core_views.signup, name='signup'),

]
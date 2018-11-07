from django.urls import path
from .views import cms
from .url_patterns import courses, users
from django.conf.urls import url
from django.urls import include

urlpatterns = [
    url(r'^$', cms.index, name='index'),
    url(r'^courses/', include(courses)),
    url(r'^users/', include(users))
]

from django.urls import path
from cms.views import users
from django.conf.urls import url

urlpatterns = [
    url(r'^signup/', users.signup, name='user_signup'),
    #  url(r'^$', courses.index, name='courses_index'),
]

from django.urls import path
from . import main_views

urlpatterns = [
    path('', main_views.index)
]

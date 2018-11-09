from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from cms.models import *



class SignUpForm(UserCreationForm):
    name = forms.CharField(max_length=150, required=False, help_text='Optional.')
    registry = forms.IntegerField(required=False, help_text='Optional.')
    email = forms.CharField(max_length=150, help_text='Required. Inform a valid email address.')

    class Meta:
        model = RegisteredUser
        fields = ('email', 'name', 'registry', )
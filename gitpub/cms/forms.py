from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from cms.models import RegisteredUser


class SignUpForm(UserCreationForm):
   name = forms.CharField(max_length=120, required=True, help_text='Full name')
   username = forms.CharField(max_length=150, required=True, help_text='Username')
   registry = forms.IntegerField(required=True, help_text='University Registry')
   email = forms.CharField(max_length=150, required=True, help_text='Required. Inform a valid email address.')

   class Meta:
      model = RegisteredUser
      fields = ('email', 'username', 'name', 'registry', 'password1', 'password2')

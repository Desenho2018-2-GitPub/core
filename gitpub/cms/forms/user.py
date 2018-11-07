from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    name = forms.CharField(max_length=120, required=True, help_text='Full Name')
    username = forms.CharField(max_length=150, required=True, help_text='Username')
    email = forms.CharField(max_length=150, required=True, help_text='Email')
    registry = forms.IntegerField(help_text='University Registry', required=True)

    class Meta:
        model = User
        fields = ('name', 'username', 'email', 'registry', 'password1', 'password2')

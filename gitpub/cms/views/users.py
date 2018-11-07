from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from gitpub.logging import debug
from cms import forms


@debug
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('name')
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            registry = form.cleaned_data.get('registry')
            raw_password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})

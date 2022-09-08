from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


def login_page(request):
    if request.method == 'POST':
        email = request.POST['user_name']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home_page')
        else:
            login_form = LoginForm(request.POST)
    else:
        login_form = LoginForm()

    return render(request, 'UserAuth/login.html', {'form': login_form})


def register_page(request):
    if request.method == 'POST':
        register_form = RegistrationForm(request.POST)
        if register_form.is_valid():
            user = register_form.save()
            login(request, user)
            return redirect('home_page')
    else:
        register_form = RegistrationForm()

    return render(request, 'UserAuth/register.html', {'form': register_form})


def forget_page(request):
    return render(request, 'UserAuth/forget.html')


def plans_page(request):
    return render(request, 'UserAuth/plans.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect('login_page')

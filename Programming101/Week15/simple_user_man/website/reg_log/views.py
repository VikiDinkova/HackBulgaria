from django.shortcuts import render, redirect
from .models import User
from .helpers import *
from django.core.urlresolvers import reverse


def home(request):
    return render(request, 'home.html', {})


def register(request):
    if request.method == "POST":

        email = request.POST["email_register"]
        password = request.POST["password_register"]

        if not user_exists(email):
            user = User(email=email, password=password)
            user.save()
            succsess = 'Succsessful registration'
            return redirect(reverse('profile'))
        else:
            error = 'User already exists'

    return render(request, 'register.html', locals())


def login(request):
    if request.method == "POST":

        email = request.POST["email_register"]
        password = request.POST["password_register"]

        if user_exists(email):
            session_key = request.POST.get(email)
            session_value = request.POST.get(password)
            request.session[session_key] = session_value
            return redirect(reverse('profile'))
        else:
            no_login = "Wrong email or password"

    return render(request, 'login.html', locals())


def logout(request):
    request.session.flush()
    return redirect(reverse('login'))


def profile(request):
    return render(request, 'profile.html', locals())

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from .forms import UserRegistrationForm


def register(request) -> HttpResponse:
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"{username}, Your account has been created! You are able to login now.")
            return redirect("users:login")
    else:
        form = UserRegistrationForm()

    return render(request, 'users/register.html', {
        'form': form
    })


def custom_logout(request) -> HttpResponse:
    logout(request)

    return render(request, "users/logout.html")

@login_required
def profile(request) -> HttpResponse:
    return render(request, "users/profile.html")
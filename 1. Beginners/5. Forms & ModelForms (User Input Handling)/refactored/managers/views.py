from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.db import IntegrityError

from .forms import ManagerForm, Manager


def managers(request) -> HttpResponse:

    managers = Manager.objects.all()

    form = ManagerForm()

    if request.method == "POST":
        form = ManagerForm(request.POST)

        if form.is_valid():
            form.save()
            
            username = form.cleaned_data.get("username")
            messages.success(request, f"Manager {username} has been added.")

            redirect("managers:add")


    return render(request, "managers/managers.html", context={
        'title': "Managers",
        'managers': managers,
        'form': form
    })
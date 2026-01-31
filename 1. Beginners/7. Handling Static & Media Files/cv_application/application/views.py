from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib import messages
from django.http import Http404

from .forms import CVForm
from .models import CV


def home(request) -> HttpResponse:
    applications = CV.objects.all()

    context: dict = {
        'applications': applications,
        'title': "Home"
    }
    
    return render(request, "home/index.html", context=context)


def application(request) -> HttpResponse:
    form = CVForm()

    if request.method == 'POST':
        form = CVForm(request.POST, request.FILES)

        if form.is_valid():
            name = form.cleaned_data.get("name")
            form.save()

            # messages.success(request, f"Application for {name} created successfully.")

            return redirect("cv:home")

    context: dict = {
        'form': form,
        'title': "Application"
    }

    return render(request, "application/index.html", context=context)

def edit(request) -> HttpResponse:
    pk: int = request.GET.get("id")
    form = CVForm()

    # if request.method == 'POST':
    #     form = CVForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         form.save()

    application = get_object_or_404(CV, id=pk)
    context: dict = {
        'app': application,
        'form': form,
        'title': f"Edit - {pk}",
    }

    return render(request, "application/edit.html", context=context)

def delete(request) -> HttpResponse:
    pk: int = request.GET.get("id")

    try:
        application = CV.objects.get(id=pk)
    except CV.DoesNotExist:
        raise Http404(f"The CV with id {pk} doesn't exist.")
    else:
        application.delete()

    return redirect("cv:home")
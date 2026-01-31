from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.http import Http404, HttpRequest
from django.contrib import messages

from .forms import AgendaForm, AgendaEditForm
from .models import Agenda


def home(request: HttpRequest) -> HttpResponse:
    agendas = Agenda.objects.all()

    settings: dict = {
        'title': "Home - Agenda",
        'agendas': agendas,
    }

    return render(request, 'agenda/home.html', context=settings)


def add(request: HttpRequest) -> HttpResponse:
    form = AgendaForm()

    if request.method == 'POST':
        form = AgendaForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data.get('name')
            due_date = form.cleaned_data.get('due_date')

            messages.info(request, f"Agenda '{name}' due on <{due_date}> added successfully.")
            form.save()

            return redirect('agenda:home')

    settings: dict = {
        'title': "Add New Agenda",
        'form': form,
    }

    return render(request, 'agenda/add.html', context=settings)


def delete(request: HttpRequest, pk: int) -> HttpResponse:
    try:
        agenda = Agenda.objects.get(id=pk)
    except Agenda.DoesNotExist:
        raise Http404(f"Agenda with ID '{pk}' doesn't exit")
    
    confirmation: str = request.GET.get('confirm')

    if confirmation:
        if confirmation == 'yes':
            agenda.delete()
            messages.warning(request, f"<{agenda.name}> due <{agenda.due_date}> has been deleted succesfully.")
            return redirect('agenda:home')
        else:
            return redirect('agenda:home')

    settings: dict = {
        'title': f"Delete Agenda - {pk}",
        'agenda': agenda,
    }
    return render(request, 'agenda/delete.html', context=settings)


def edit(request: HttpRequest, pk: int) -> HttpResponse:
    agenda = get_object_or_404(Agenda, id=pk)

    form = AgendaEditForm(instance=agenda)

    if request.method == 'POST':
        form = AgendaEditForm(request.POST, instance=agenda)
        if form.is_valid():
            form.save()
            
            messages.info(request, f"<{agenda.name }> has been updated successfully.")
            return redirect('agenda:home')

    settings: dict = {
        'title': f"Edit Agenda - {pk}",
        'agenda': agenda,
        'form': form,
    }

    return render(request, 'agenda/edit.html', context=settings)
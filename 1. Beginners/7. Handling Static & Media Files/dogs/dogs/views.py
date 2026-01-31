from django.shortcuts import render, redirect, get_object_or_404, HttpResponse

from .forms import DogForm, Dog
from core.App.Enums.RequestMethods import RequestMethods


def list(request) -> HttpResponse:
    dogs = Dog.objects.all()

    context = {
        'dogs': dogs
    }

    return render(request, "dogs/list.html", context=context)

# 
def upload(request) -> HttpResponse:
    form = DogForm()

    if request.method == RequestMethods.POST:
        form = DogForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("dogs:list")

    context_data: dict = {
        'form': form
    }

    return render(request, "dogs/index.html", context=context_data)

def delete(request, pk: int) -> HttpResponse:
    dog = get_object_or_404(Dog, pk=pk)
    if dog:
        dog.delete()

    return redirect("dogs:list")
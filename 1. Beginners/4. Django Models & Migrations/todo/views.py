from django.shortcuts import render, HttpResponse

def home(request) -> HttpResponse:
    """View for the home page of todo"""
    return render(request, "todo/home.html")


def create(request) -> HttpResponse:
    """View for the crate page of todo"""
    return render(request, "todo/create.html")
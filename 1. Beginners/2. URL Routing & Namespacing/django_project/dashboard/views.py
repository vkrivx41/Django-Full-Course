from django.shortcuts import render, HttpResponse

def dashboard(request) -> HttpResponse:
    """the dashboard page view"""
    
    return HttpResponse("<h1>Dashboard</h1>")


def analytics(request) -> HttpResponse:
    """the dashboard analytics page view"""
    
    return HttpResponse("<h1>Dashboard Analytics</h1>")
from django.shortcuts import render, HttpResponse

def dashboard(request) -> HttpResponse:
    """the dashboard page view"""
    
    return render(request, "dashboard.html")

def analytics(request) -> HttpResponse:
    """the dashboard analytics page view"""
    
    return render(request, "analytics.html")
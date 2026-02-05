from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


class BaseView(View):
    def get(self, request) -> HttpResponse:
        return HttpResponse("<h1>HTTP GET Response - Visit /products for more...</h1>")
    
    def post(self, request) -> HttpResponse:
        return HttpResponse("<h1>HTTP POST Response - Visit /products for more...</h1>")


class ProductsView(View):
    def get(self, request) -> HttpResponse:
        return render(request, 'base/index.html')
    
    def post(self, request) -> HttpResponse:
        return HttpResponse("<h1>HTTP POST Response</h1>")
    
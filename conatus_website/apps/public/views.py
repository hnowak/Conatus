from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name='index.html', context={})


def about(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name='about.html', context={})
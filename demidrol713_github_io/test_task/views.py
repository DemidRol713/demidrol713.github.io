from django.http import HttpResponse
from django.shortcuts import render


def task_url(request):
    name = request.GET.get('name')
    message = request.GET.get('message')
    return HttpResponse(f'Hello {name}! {message}!')
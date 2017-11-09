from django.shortcuts import render

# Create your views here.
from django import views
from django.http import HttpResponse


def index(request):
    return HttpResponse('hello world')

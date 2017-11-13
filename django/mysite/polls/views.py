from django.shortcuts import render

# Create your views here.
from django import views
from django.http import HttpResponse
import time

def index(request):
    return HttpResponse('hello world %s' % time.strftime('%Y-%m-%d %H:%M:%S'))

def detail(request,req_id):
    return HttpResponse('hello world %s,id:%s' % (time.strftime('%Y-%m-%d %H:%M:%S'),req_id))

def result(request,req_id):
    return HttpResponse('hello world %s,id:%s' % (time.strftime('%Y-%m-%d %H:%M:%S'), req_id))

def vote(request,req_id):
    return HttpResponse('hello world %s,id:%s' % (time.strftime('%Y-%m-%d %H:%M:%S'), req_id))

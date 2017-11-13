from django.shortcuts import render

# Create your views here.
from django import views
from django.http import HttpResponse
from django.template import loader
import time

def index(request):
    from .models import Question
    last = Question.objects.order_by('pub_date')[:5]
    template = loader.get_template('polls/index.html')
    info = {
        'list':last
    }
    return HttpResponse(template.render(info,request))

def detail(request,req_id):
    return HttpResponse('hello world %s,id:%s' % (time.strftime('%Y-%m-%d %H:%M:%S'),req_id))

def result(request,req_id):
    return HttpResponse('hello world %s,id:%s' % (time.strftime('%Y-%m-%d %H:%M:%S'), req_id))

def vote(request,req_id):
    return HttpResponse('hello world %s,id:%s' % (time.strftime('%Y-%m-%d %H:%M:%S'), req_id))

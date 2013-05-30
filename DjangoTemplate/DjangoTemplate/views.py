'''
Created on 2013-5-20

@author: mike
'''
from django.http import HttpResponse, Http404
import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render_to_response



def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def current_datetime_t(request):
    now = datetime.datetime.now()
    t = Template("<html><body>It is now {{ current_date }}.</body></html>")
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)

def current_datetime_t_split(request):
    now = datetime.datetime.now()
    t = get_template('current_datetime.html')
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)

def current_datetime_simple(request):
    print("simple model")
    now = datetime.datetime.now()
    return render_to_response('current_datetime.html', {'current_date': now})

def current_datetime_sub1(request):
    print("simple model")
    now = datetime.datetime.now()
    return render_to_response('sub/current_datetime_1.html', {'current_date': now})

def current_datetime_sub2(request):
    print("current_datetime_sub2")
    now = datetime.datetime.now()
    raise Http404
    return render_to_response('sub/current_datetime_2.html', {'current_date': now})

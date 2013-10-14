from django.http import HttpResponse, Http404
from django.shortcuts import render
import datetime

def hello(request):
    return HttpResponse("Hello world")

def old_current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def current_datetime(request):
    now = datetime.datetime.now()
    return render(request, 'current_datetime.html', {'current_date': now})

def old_hours_ahead(request, offset):#offset is the string captured by the parentheses in the URLpattern
    try:
        offset = int(offset)#converts the string value to an integer
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset) #timedelta function requires the hours parameter to be an integer.
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)

def hours_ahead(request, offset):#offset is the string captured by the parentheses in the URLpattern
    try:
        offset = int(offset)#converts the string value to an integer
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset) #timedelta function requires the hours parameter to be an integer.
    return render(request, 'hours_ahead.html', {'hour_offset':offset, 'next_time':dt})

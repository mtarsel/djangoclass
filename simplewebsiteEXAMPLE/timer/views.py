from django.http import HttpResponse, Http404
import datetime

def hello(request):
    return HttpResponse("Hello world")

#def error404(request):
#    return render(request,'404.html')

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


def hours_ahead(request, offset):#offset is the string captured by the parentheses in the URLpattern
    try:
        offset = int(offset)#converts the string value to an integer
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
#timedelta function requires the hours parameter to be an integer.
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)

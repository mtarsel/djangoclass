from django.shortcuts import render_to_response

def error404(request):
    return render(request,'404.html')

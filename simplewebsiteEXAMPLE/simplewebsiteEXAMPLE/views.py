from django.shortcuts import render_to_response, render

def error404(request):
    return render(request,'404.html')

def home(request):
    return render(request,'home.html')

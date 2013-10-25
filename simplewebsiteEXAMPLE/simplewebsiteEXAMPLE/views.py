from django.shortcuts import render

def error404(request):
    return render(request,'404.html')

def home(request):
    return render(request,'home.html')

def thankyou(request):
    return render(request,'thankyou.html')

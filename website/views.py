from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'website/index.html', locals())

def about(request):
    return render(request, 'website/about.html', locals())
from django.shortcuts import render
from .models import *

def homepage(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def blog(request):
    maqolalar = Article.objects.all()
    return render(request, 'blog.html', {'maqolalar':maqolalar})

def maqola(request, num):
    maqola = Article.objects.get(id=num)
    rasmlar = Photos.objects.filter(article=maqola)
    return render(request, 'maqola.html', {'maqola':maqola, 'rasmlar':rasmlar})

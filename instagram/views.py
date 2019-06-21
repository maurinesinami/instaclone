from django.shortcuts import render
from django.http import HttpResponse,Http404
from . models import Image






def welcome(request):
    images = Image.objects.all()
    return render(request,'index.html',{"images":images})

from django.shortcuts import render
from django.http import HttpResponse,Http404
from . models import Image
from django.contrib.auth.decorators import login_required




@login_required(login_url='/accounts/login/')
def welcome(request):
    images = Image.objects.all()
    return render(request,'index.html',{"images":images})

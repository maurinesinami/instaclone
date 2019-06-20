from django.shortcuts import render
from django.http import HttpResponse,Http404







def welcome(request):
    return render(request,'index.html')

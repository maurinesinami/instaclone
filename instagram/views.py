from django.shortcuts import render
from django.http import HttpResponse,Http404







def welcome(request):
    return HttpResponse('welcome to instagram')

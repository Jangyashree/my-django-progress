from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def biriyani(request):
    return HttpResponse('Biriyani is my fav')
def kabab(request):
    return HttpResponse('<marquee>I love Kabab</marquee>')
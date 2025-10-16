from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def icecream(request):
    return HttpResponse('All time Fav')
def kitkat(request):
    return HttpResponse('i love Kitkat')
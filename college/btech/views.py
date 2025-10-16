from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def studentbranch(request):
    return HttpResponse('<h1>Bachelors Of Technology</h1>')
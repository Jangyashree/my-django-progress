from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def studentbranch(request):
    return HttpResponse('<h1>Bachelor of computer science<h1>')
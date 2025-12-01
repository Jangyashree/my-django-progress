from django.shortcuts import render

# Create your views here.
from app.models import *
from django.views.generic import ListView

class school_list(ListView):
    model=School
    #queryset=School.objects.filter(name='QSPIDERS')
    #template_name='school_list.html'
    context_object_name='QSLSO'
    ordering = ['scname']

    
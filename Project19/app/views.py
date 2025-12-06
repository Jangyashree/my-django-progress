from django.shortcuts import render

# Create your views here.
from app.models import *
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class Home(TemplateView):
    template_name='app/Home.html'

class school_list(ListView):
    model=School
    #queryset=School.objects.filter(name='QSPIDERS')
    #template_name='school_list.html'
    context_object_name='QSLSO'
    ordering = ['scname']

class SchoolDetail(DetailView):
    model=School
    context_object_name='RetrieveSO'

class SchoolCreate(CreateView):
    model=School
    fields='__all__'

class SchoolUpdate(UpdateView):
    model=School
    fields='__all__'


class SchoolDelete(DeleteView):
    model=School
    context_object_name='SCO'
    success_url=reverse_lazy('school_list')


    
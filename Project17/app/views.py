from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.forms import *
from django.views.generic import View, TemplateView

#FBV Return String
def FBV(request):
    return HttpResponse('FBV')

#CBV returning string 
class CBV(View):
    def get(self,request):
        return HttpResponse('This is CBV')

#FBV returning a html page

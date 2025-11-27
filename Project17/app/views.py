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
def FBV_template(request):
    return render(request,'FBV_template.html')

#CBV returning a html page
class CBV_template(View):
    def get(self,request):
        return render(request,'CBV_template.html')
        
#validating Form by using FBV
def FBV_form(request):
    EFORM=SchoolMF()
    if request.method=='POST':
        SFORM=SchoolMF(request.POST)
        if SFORM.is_valid():
            SFORM.save
            return HttpResponse('Data inserted')
        
    return render(request,'FBV_form.html',{'EFORM':EFORM})

#validating Form by using CBV
class CBV_form(View):
    def get(self, request):
        form = SchoolMF()
        return render(request, 'CBV_form.html', {'form': form})

    def post(self, request):
        form = SchoolMF(request.POST)
        if form.is_valid():
            return HttpResponse("Data inserted")
        return render(request, 'CBV_form.html', {'form': form})


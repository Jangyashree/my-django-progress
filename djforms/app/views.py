from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse

# Create your views here.
def studentdjform(request):
    ESDJF=StudentdjForm()
    d={'ESDJF':ESDJF}
    if request.method=='POST':
        SFDO=StudentdjForm(request.POST) #collect data
        if SFDO.is_valid():  # for validating
            return HttpResponse(str(SFDO.cleaned_data))
        else:
            return HttpResponse('Invalid data')
              
    return render(request,'studentdjform.html',d)




def insert_student(request):
    ESDJFO=StudentdjForm()
    d = {'ESDJFO':ESDJFO}
    if request.method=='POST':
        SDJFO=StudentdjForm(request.POST)
        if SDJFO.is_valid():
            return HttpResponse(str(SDJFO.cleaned_data))
        else:
            return HttpResponse('Invalid data')
              
    return render(request,'insert_student.html',d)
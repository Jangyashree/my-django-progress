from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.

def insert_student(request):
    ESMDFO=StudentModelForm()
    d={'ESMDFO':ESMDFO}
    
    if request.method=='POST':
        SMDFO=StudentModelForm(request.POST)
        if SMDFO.is_valid():
            SMDFO.save()
            return HttpResponse('Inserted')
        else:
            return HttpResponse('Invalid data')

    return render(request,'insert_student.html',d)
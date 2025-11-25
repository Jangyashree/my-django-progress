from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse

def registration(request):
    EDMFO=DeptMF()
    EEMFO=EmpMF()
    d={'EDMFO':EDMFO, 'EEMFO':EEMFO}

    if request.method=='POST':
        NMDMFDO=DeptMF(request.POST)
        NMEMFDO=EmpMF(request.POST)

        if NMDMFDO.is_valid() and NMEMFDO.is_valid():
        
            MDMFDO=NMDMFDO.save(commit=False)
            MDMFDO.save()

            MEMFDO=NMEMFDO.save(commit=False)
            MEMFDO.dept_no=MDMFDO
            MEMFDO.save()
            
            return HttpResponse('Registration Successfully.')
        else:
            return HttpResponse('Invalid Data')
    
    
    
    return render(request,'registration.html',d)

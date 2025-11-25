from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse

def insertdata(request):
    ETMFO=TopicMF()
    EWMFO=WebpageMF()
    EAMFO=AccessrecordMF()
    d={'ETMFO':ETMFO , 'EWMFO':EWMFO , 'EAMFO':EAMFO}

    if request.method=='POST':
        NMTMFDO=TopicMF(request.POST)
        NMWMFDO=WebpageMF(request.POST)
        NMAMFDO=AccessrecordMF(request.POST)

        if NMTMFDO.is_valid() and NMWMFDO.is_valid() and NMAMFDO.is_valid():
            MTMFDO=NMTMFDO.save(commit=False)
            MTMFDO.save()

            MWMFDO=NMWMFDO.save(commit=False)
            MWMFDO.topic_name=MTMFDO
            MWMFDO.save()

            MAMFDO=NMAMFDO.save(commit=False)
            MAMFDO.name=MWMFDO
            MAMFDO.save()

            return HttpResponse('Data is Inserted')
        else:
            return HttpResponse('Invalid Data')


    return render(request,'insertdata.html',d)
from django.shortcuts import render

# Create your views here.
from app.models import *
from app.forms import *
from django.http import HttpResponse

def insert_topic(request):
    ETDFO=TopicDjForm()
    d={'ETDFO':ETDFO}
    
    if request.method=='POST':
        TDFDO=TopicDjForm(request.POST)
        if TDFDO.is_valid():
            tn=TDFDO.cleaned_data['topic_name']
            TTO=Topic.objects.get_or_create(topic_name=tn)
            if TTO[1]:
                return HttpResponse('New Topic Created')
            else:
                return HttpResponse('Topic is Already Present')
        else:
            return HttpResponse('Invalid Data')

    return render(request,'insert_topic.html',d)


def insert_webpage(request):
    EWDFO=WebpageDjForm()
    d={'EWDFO':EWDFO}
    
    if request.method=='POST':
        WDFDO=WebpageDjForm(request.POST)
        if WDFDO.is_valid():
            TO=WDFDO.cleaned_data['topic_name']
            na=WDFDO.cleaned_data['name']
            ur=WDFDO.cleaned_data['url']
            TWO=Webpage.objects.get_or_create(topic_name=TO,name=na,url=ur)      
            if TWO[1]:
                return HttpResponse('Webpage is Created')
            else:
                return HttpResponse('Webpage is Already Present')
    
    return render(request,'insert_webpage.html',d)


def insert_accessrecord(request):
    EADFO=AccessDjForm()
    d={'EADFO':EADFO}
    if request.method=='POST':
        ADFDO=AccessDjForm(request.POST)
        if ADFDO.is_valid():
            WO=ADFDO.cleaned_data['name']
            auth=ADFDO.cleaned_data['author']
            date=ADFDO.cleaned_data['date']
            WAO=Accessrecord.objects.get_or_create(name=WO,author=auth,date=date)
            if WAO[1]:
                return HttpResponse('Accessrecord is Created')
            else:
                return HttpResponse('Accessrecord Already Present')

    return render(request,'insert_accessrecord.html',d)
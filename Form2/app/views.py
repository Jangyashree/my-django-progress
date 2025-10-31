from django.shortcuts import render

# Create your views here.
from app.models import *
from django.http import HttpResponse


def display_topic(request):
    QLTO=Topic.objects.all()
    d={'QLTO':QLTO}
    return render(request,'display_topic.html',d)


def display_webpage(request):
    QLWO=Webpage.objects.all()
    d={'QLWO':QLWO}
    return render(request,'display_webpage.html',d)

def display_access(request):
    QLAO=Accessrecord.objects.all()
    d={'QLAO':QLAO}
    return render(request,'display_access.html',d)


def insert_topic(request):
    if request.method=='POST':
        tn=request.POST['tn']
        TTO=Topic.objects.get_or_create(topic_name=tn)
        if TTO[1]:
            return HttpResponse('New Topic is Created')
        else:
            return HttpResponse('Topic is already exist')
    return render(request,'insert_topic.html')


def insert_webpage(request):
    if request.method == 'POST':
        TO = Topic.objects.filter()
        if TO: 
            na = request.POST['na']
            ur = request.POST['ur']
        
            TWO = Webpage.objects.get_or_create(topic_name=TO[0],name=na,url=ur)
            if TWO[1]:
                QLWO = Webpage.objects.all()
                d = {'QLWO':QLWO}
                return render(request,'display_webpage.html',d)
            else:
                return render(request,'insert_webpage.html')
        else:
            return render(request,'insert_topic.html')

    return render(request,'insert_webpage.html')


def insert_accessrecord(request):
    if request.method == 'POST':
        wid = request.POST['wid']     
        auth = request.POST['auth'] 
        date = request.POST['date'] 

        LWO=Webpage.objects.filter(id=wid)
        if LWO:
            Wo = LWO[0]
            TARO=Accessrecord.objects.get_or_create(name=Wo,author=auth,date=date)
            if TARO[1]:
                QLAO=Accessrecord.objects.all()
                d={'QLAO':QLAO}
                return render(request,'display_access.html',d)
            else:
                return render(request,'insert_accessrecord.html')
        else:
            return render(request,'insert_webpage.html')
    
    return render(request,'insert_accessrecord.html')
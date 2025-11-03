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
            QLTO=Topic.objects.all()
            d={'QLTO':QLTO}
            return render(request,'display_topic.html',d)
        else:
            return HttpResponse('Topic is already exist')
    return render(request,'insert_topic.html')


def insert_webpage(request):
    QLTO = Topic.objects.all()
    d={'QLTO':QLTO}

    if request.method == 'POST':
        tn=request.POST['tn']
        TO = Topic.objects.get(topic_name=tn)
        na = request.POST['na']
        ur = request.POST['ur']
        TWO = Webpage.objects.get_or_create(topic_name=TO,name=na,url=ur)
        if TWO[1]:
            QLWO = Webpage.objects.all()
            d = {'QLWO':QLWO}
            return render(request,'display_webpage.html',d)
        else:
            return HttpResponse('Already Present')

    return render(request,'insert_webpage.html',d)



def insert_accessrecord(request):
    QLWO = Webpage.objects.all()
    d={'QLWO':QLWO}
    
    if request.method == 'POST':
        na = request.POST['na']     
        auth = request.POST['auth'] 
        date = request.POST['date'] 
        WO=Webpage.objects.get(id=na)

        TARO=Accessrecord.objects.get_or_create(name=WO,author=auth,date=date)
        if TARO[1]:
            QLAO=Accessrecord.objects.all()
            d={'QLAO':QLAO}
            return render(request,'display_access.html',d)
        else:
            return HttpResponse('Accessrecord is already Present')

    return render(request,'insert_accessrecord.html',d)


def select__multiple_topic(request):
    QLTO = Topic.objects.all()
    d={'QLTO':QLTO}
    if request.method == "POST":
        STL = request.POST.getlist('tn')
        

        EWQS = Webpage.objects.none()
        for TO in STL:
            EWQS = EWQS | Webpage.objects.filter(topic_name=TO)
        d1 = {'EWQS':EWQS}
        return render(request,'display_webpage.html',d1)

    return render(request,'select__multiple_topic.html',d)
    

def select_multiple_webpage(request):
    QLWO = Webpage.objects.all()
    d={'QLWO':QLWO}
    if request.method == "POST":
        SWL = request.POST.getlist('na')
        print(SWL)

        QLAO = Webpage.objects.none() #Empty Queryset
        for WO in SWL:
            QLAO = QLAO | Accessrecord.objects.filter(name=WO)
        d1 = {'QLAO':QLAO}
        return render(request,'display_access.html',d1)
    
    return render(request,'select_multiple_webpage.html',d)


#action attribute(checkbox)
def checkbox(request):
    QLTO=Topic.objects.all()
    d={'QLTO':QLTO}
    return render(request,'checkbox.html',d)


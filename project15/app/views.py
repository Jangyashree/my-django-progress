from django.shortcuts import render
from app.models import *
# Create your views here.
from django.http import HttpResponse

def insert_topic(request):
    tn=input('enter topic name')
    TTO=Topic.objects.get_or_create(topic_name=tn)
    if TTO[1]:
        return HttpResponse('Topic is created')
    else:
        return HttpResponse('Topic is already present')
   
    
def insert_webpage(request):
    tn=input('enter topic name')
    Lto=Topic.objects.filter(topic_name=tn)
    if Lto:
        To=Lto[0]
        name=input('enter a name for webpage')
        url=input('enter a url')
        TWo=Webpage.objects.get_or_create(topic_name=To,name=name,url=url)

        if TWo[1]:
            return HttpResponse('one row is created in webpage')
        else:
            return HttpResponse('Given input is already present')
    else:
        return HttpResponse('Given Topic name is not present in Topic Table')
    

   
def insert_accessrecord(request):
    Wid=int(input('webpageid'))
    LWo=Webpage.objects.get(id=Wid)
    if LWo:
        Wo=LWo[0]
        author=input('enter name of author')
        date=input('enter date in this fromat yyyy-mm-dd')
        TARO=Accessrecord.objects.get_or_create(name=Wo,author=author,date=date)
        if TARO[1]:
            return HttpResponse('one row is created in accessrecord')
        else:
            return HttpResponse('Given input already present')
    else:
        return HttpResponse('Given webpage name is not present in webpage Table')



def display_topic(request):
    QLAO=Topic.objects.all()
    
    d={'QLAO':QLAO}
    return render(request,'display_topic.html',d)


def display_webpage(request):
    QLAO=Webpage.objects.all()
    QLAO=Webpage.objects.filter(id__in=(1,4))
    QLAO=Webpage.objects.filter(id__range=(2,4))
    QLAO=Webpage.objects.filter(id__gte=2)
    QLAO=Webpage.objects.filter(id__gt=2)
    QLAO=Webpage.objects.filter(id__lt=2)
    QLAO=Webpage.objects.filter(id__lte=2)
    QLAO=Webpage.objects.filter(name__startswith='R')
    QLAO=Webpage.objects.filter(name__endswith='k')
    QLAO=Webpage.objects.filter(name__contains='R')
    QLAO=Webpage.objects.filter(name__regex='^M\w*')
    QLAO=Webpage.objects.filter(name__isnull=False)
    QLAO=Webpage.objects.filter(name__isnull=False)

    d={'QLAO':QLAO}
    return render(request,'display_webpage.html',d)



def display_access(request):
    QLAO=Accessrecord.objects.all()
    QLAO=Accessrecord.objects.filter(date='2025-1-10')
    QLAO=Accessrecord.objects.filter(date__month='4')
    QLAO=Accessrecord.objects.filter(date__year=2025)
    QLAO=Accessrecord.objects.filter(date__day='10')
    
    d={'QLAO':QLAO}
    return render(request,'display_access.html',d)

    
def topicwebpagejoin(request):

    QLTWO=Webpage.objects.all()
    d={'QLTWO':QLTWO}
    return render(request,'topicwebpagejoin.html',d)


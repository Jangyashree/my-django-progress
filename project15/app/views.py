from django.shortcuts import render
from app.models import *
# Create your views here.
from django.http import HttpResponse

from project15 import urls

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
    
    QLWO=Webpage.objects.filter(id__in=(1,4))
    QLWO=Webpage.objects.filter(id__range=(2,4))
    QLWO=Webpage.objects.filter(id__gte=2)
    QLWO=Webpage.objects.filter(id__gt=2)
    QLWO=Webpage.objects.filter(id__lt=2)
    QLWO=Webpage.objects.filter(id__lte=2)
    QLWO=Webpage.objects.filter(name__startswith='R')
    QLWO=Webpage.objects.filter(name__endswith='k')
    QLWO=Webpage.objects.filter(name__contains='R')
    QLWO=Webpage.objects.filter(name__regex='^M\w*')
    QLWO=Webpage.objects.filter(name__isnull=False)
    QLWO=Webpage.objects.filter(name__isnull=False)

    QLWO=Webpage.objects.all()

    d={'QLWO':QLWO}
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


def update_webpages(request):
    #Updating Query
    #Webpage.objects.filter(topic_name='ab').update(url='https://www.AB.com')
    #Webpage.objects.filter(name='remo').update(url='https://www.RemoDancer.com')
    #Webpage.objects.filter(name='Remo').update(topic_name='Dancer')
    

    #Webpage.objects.update_or_create(name='Ronaldo',defaults={'url':'https://ronaldo.com'})
    #Webpage.objects.update_or_create(name='Harshad',defaults={'url':'https://python.com'})
    #Webpage.objects.update_or_create(topic_name='Harshad',defaults={'url':'https://python.com'})

    #CTO=Topic.objects.get(topic_name='Cricket')
    #Webpage.objects.update_or_create(name='Virat',defaults={'topic_name':CTO})

    #Webpage.objects.update_or_create(name='Rohit',defaults={'topic_name':CTO})

    #After Updation We are etching all Data
    QLWO=Webpage.objects.all()
    d={'QLWO':QLWO}
    return render(request,'display_webpage.html',d)

def delete_webpage(request):
    #Deleting a Specific record
    Webpage.objects.filter(name='Rohit').delete()

    #Fetching data
    QLWO=Webpage.objects.all().delete()

    d={'QLWO':QLWO}
    return render(request,'display_webpage.html',d)

def wish(request,name):
    return HttpResponse(f'Hello {name} How Are You!')
from django.shortcuts import render

# Create your views here.
def filter(request):
    import datetime
    dt=datetime.datetime.now()
    d={'data':'Hai Python How are YOu','c':1,'dt':dt}

    return render(request,'filter.html',d)
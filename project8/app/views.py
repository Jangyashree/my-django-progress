from django.shortcuts import render

# Create your views here.
def loop(request):
    d={'l':[10,20,30,40],'name':'Hello'}
    return render(request,'loop.html',d)

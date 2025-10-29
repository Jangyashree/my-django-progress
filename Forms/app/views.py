from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def htmlforms(request):
    if request.method == 'POST':
        un = request.POST['una']
        pw = request.POST['pwa']
        return HttpResponse(f'username is {un} and Password is {pw}')
     
    return render(request,'htmlforms.html')
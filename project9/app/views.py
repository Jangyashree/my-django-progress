from django.shortcuts import render

# Create your views here.
def boy(request):
    return render(request,'boy.html')

def girl(request):
    return render(request,'girl.html')
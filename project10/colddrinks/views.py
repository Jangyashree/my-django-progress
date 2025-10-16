from django.shortcuts import render

# Create your views here.
def sprite(request):
    return render(request,'sprite.html')
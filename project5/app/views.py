from django.shortcuts import render

# Create your views here.
def table(request):
    return render(request,'table.html')

def jspiders(request):
    return render(request,'jspiders.html')

def loginform(request):
    return render(request,'loginform.html')

def login(request):
    return render(request,'login.html')

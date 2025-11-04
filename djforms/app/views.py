from django.shortcuts import render
from app.forms import *
# Create your views here.
def studentdjform(request):
    ESDJF=StudentdjForm()
    d={'ESDJF':ESDJF}
    return render(request,'studentdjform.html',d)
from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from app.serializers import *
from rest_framework.viewsets import ViewSet,ModelViewSet
from app.models import *

class StudentCrudByVS(ViewSet):
    def list(self,request):
        QLSTO=Student.objects.all() 
        SJO=StudentMS(QLSTO,many=True)
        return Response(SJO.data)
    
    def retrieve(self,request,pk):
        SO=Student.objects.get(pk=pk)
        JO=StudentMS(SO)
        return Response(JO.data)
    
    def update(self,request,pk):
        JD=request.data
        SO=Student.objects.get(pk=pk)
        SORMO=StudentMS(SO,data=JD)
        if SORMO.is_valid():
            SORMO.save()
            return Response({'Success':'Data is Updated'})
        else:
            return Response({'Invalid':'Data is Not Valid'})

    def partial_update(self,request,pk):
        JD=request.data
        SO=Student.objects.get(pk=pk)
        SORMO=StudentMS(SO,data=JD,partial=True)
        if SORMO.is_valid():
            SORMO.save()
            return Response({'Success':'Data is updated'})
        else:
            return Response({'Invalid':'Data is Not Valid'})

    def destroy(self,request,pk):
        SO=Student.objects.get(pk=pk)
        SO.delete()
        return Response({'Deleted':'Data is Deleted'})

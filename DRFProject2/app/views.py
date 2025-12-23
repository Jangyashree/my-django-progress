from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from app.serializers import *
from rest_framework.views import APIView

class StudentCRUD(APIView):
    def get(self,request,pk=None):
            if pk==None:
                QLSTO=Student.objects.all() 
                SJO=StudentMS(QLSTO,many=True)
                return Response(SJO.data)
            else:
                SO=Student.objects.get(pk=pk)
                JO=StudentMS(SO)
                return Response(JO.data)
            
    def post(self,request,pk=None):
        JD=request.data
        SORMO=StudentMS(data=JD)
        if SORMO.is_valid():
            SORMO.save()
            return Response({'Success':'Data is Created'})
        else:
            return Response({'Invalid':'Data is Not Valid'})
        
    def put(self,request,pk):
        JD=request.data
        SO=Student.objects.get(pk=pk)
        SORMO=StudentMS(SO,data=JD)
        if SORMO.is_valid():
            SORMO.save()
            return Response({'Success':'Data is Updated'})
        else:
            return Response({'Invalid':'Data is Not Valid'})
           
    def patch(self,request,pk):
        JD=request.data
        SO=Student.objects.get(pk=pk)
        SORMO=StudentMS(SO,data=JD)
        if SORMO.is_valid():
            SORMO.save()
            return Response({'Success':'Data is updated'})
        else:
            return Response({'Invalid':'Data is Not Valid'})
           
    def delete(self,request,pk):
        SO=Student.objects.get(pk=pk)
        SO.delete()
        return Response({'Deleted':'Data is Deleted'})

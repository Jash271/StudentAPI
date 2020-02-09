from django.shortcuts import render
from . serializer import StudentSerializer
from rest_framework import generics
from . models import Student
from rest_framework.decorators import api_view
import json
from django.http import JsonResponse,HttpResponse
import requests
# Create your views here.
def home(request):
    return render(request,'Home.html')

class CreateStudent(generics.GenericAPIView):
    def post(self,request):
        s=StudentSerializer(data=self.request.data)
        if s.is_valid():
            s.save()
            return JsonResponse("ok",safe=False)   
        else:
            return JsonResponse('No',safe=False)     


    
class GetStudent(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=StudentSerializer
    queryset=Student.objects.all()


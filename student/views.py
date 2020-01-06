from django.shortcuts import render
from . serializer import StudentSerializer
from rest_framework import generics
from . models import Student
# Create your views here.
def home(request):
    return render(request,'Home.html')

class CreateStudent(generics.ListCreateAPIView):
    serializer_class=StudentSerializer
    queryset=Student.objects.all()

class GetStudent(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=StudentSerializer
    queryset=Student.objects.all()


from django.contrib import admin
from django.urls import  include,path
from . import views 
urlpatterns = [
    path('',views.home,name='home'), 
    path('CreateStudent',views.CreateStudent.as_view(),name='CreateStudent'),
    path('CallApi',views.callApi,name='callApi'),
    path('GetStudent/<int:pk>',views.GetStudent.as_view(),name='GetStudent'),


]
    

from django.shortcuts import render
from django.http import HttpResponse, request
# Create your views here.
def index(request):
    return HttpResponse("Hello World")

def index1(request):
    return HttpResponse('another response')

def index2(request):
     return render(request,'index.html') 
    
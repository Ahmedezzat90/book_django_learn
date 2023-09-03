from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def templat(request):
    #return HttpResponse("hi to my work")
    return render(request,'managment/managment.html')
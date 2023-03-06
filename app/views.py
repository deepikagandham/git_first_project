from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def venkey(request):
    return HttpResponse('<h1>I Will Get Job</h1>')
      

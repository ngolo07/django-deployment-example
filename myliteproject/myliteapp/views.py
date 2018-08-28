from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("hello, hope to get it now")

# Create your views here.

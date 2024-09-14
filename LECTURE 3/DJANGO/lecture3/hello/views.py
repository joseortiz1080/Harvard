from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello!")

def jose(request):
    return HttpResponse("Hello, jose")

def laura(request):
    return HttpResponse("Hello, Lalis!!")
from django.shortcuts import render , HttpResponse

# Create your views here.
def index(request): #new
    return HttpResponse('<h1>Django Include URLs</h1>')
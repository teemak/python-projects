from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'models/index.html')
    #return HttpResponse('<h1>THIS IS THE HTTPRESPONSE</h1>')

from django.shortcuts import render
from .models import Entry
#from django.http import HttpResponse

# Create your views here.
def index(request):
    entries = Entry.objects.all()
    #return HttpResponse('<h1>Hello Tee!</h1>')
    return render(request, 'myapp/index.html', {'entries': entries})

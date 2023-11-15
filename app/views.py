from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination
# Create your views here.
def index(request):
    dests = Destination.objects.all()
    return render(request,"index.html",{'dests':dests})

def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
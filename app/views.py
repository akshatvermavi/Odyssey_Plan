from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination
from django.shortcuts import render
from .Movierecommendationmodel import movie_recommendation_challange
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    dests = Destination.objects.all()
    return render(request,"index.html",{'dests':dests})

def home(request):
    return render(request,'home.html')
def create_event(request):
    return render(request,'create_event.html')
def about(request):
    return render(request,'about.html')
# def todo(request):
#     return render(request,'todo.html')
def threed(request):
    return render(request,'threed.html')

def movieform(request):
    res = [] 
    if request.method == 'POST':
        movie = request.POST.get('movie', '')
        print(movie)
        
        # Assuming movie_recommendation_challange returns a DataFrame with a 'Title' column
        res = movie_recommendation_challange(movie)
        res = list(res['Title'])

        # Pass the results as part of the dictionary in the render function
        return render(request, 'result.html', {'results': res})
    return render(request, 'result.html', {'results': res})
def predict(request):
    return render(request,'predicts.html')
  # Replace 'your_module' with the actual module name


from django.urls import path
from django.urls import path, include
from . import views


urlpatterns = [
   path('',views.index, name = 'index'),
   path('',views.home, name = "home"),
   path("about/",views.about, name="about"),
   path("threed/",views.threed,name = "threed"),
   path("create_event",views.create_event,name= "create_event"),
   path("movieform/",views.movieform,name = "movieform"),
   path("predict/",views.predict,name = "predict"),
   
   # path("create_event/",views.create_event, name="create_event"),
]
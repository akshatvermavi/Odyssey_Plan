from django.urls import path
from django.urls import path, include
from . import views


urlpatterns = [
   path('',views.index, name = 'index'),
   path('',views.home, name = "home"),
   path("about/",views.about, name="about"),
   # path("create_event/",views.create_event, name="create_event"),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Todo, name='Todo'),
    path('delete/<str:pk>', views.delete,name='delete')
  
]
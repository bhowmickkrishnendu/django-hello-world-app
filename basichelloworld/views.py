# Creating a url pattern for the hello world app.
from django.urls import path
from . import views

urlpatterns = [
    # Creating a url pattern for the hello world app.
    path('hello/', views.hello, name='basichelloworld'),
   # Creating a url pattern for the index page.
    path('', views.index, name='index'),
]

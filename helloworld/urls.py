# Creating a URL pattern for the hello view.
from django.urls import path
from . import views

urlpatterns = [
   # Creating a URL pattern for the hello view.
    path('', views.hello, name='hello'),
]

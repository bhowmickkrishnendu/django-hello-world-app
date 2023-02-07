# Importing the path and include functions from the django.urls module.
from django.urls import path, include

urlpatterns = [
    path('', include('helloworld.urls')),
]

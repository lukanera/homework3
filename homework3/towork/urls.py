from django.contrib import admin
from django.urls import path
from .views import home, about, about_stalin

urlpatterns = [
    path('home/', home),
    path('about/', about),
    path('about_stalin/', about_stalin),
]

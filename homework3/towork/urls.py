from django.contrib import admin
from django.urls import path
from .views import create_article, show_articles

urlpatterns = [
    path('create_article', create_article, name = 'create_article'),
    path('show_articles', show_articles, name = 'show_articles'),
]

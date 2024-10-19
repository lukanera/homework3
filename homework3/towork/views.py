from django.shortcuts import render, HttpResponse

def home(request):
    return HttpResponse("<h1>Hello stalin</h1>")

def about(request):
    return HttpResponse("<h1>We LOVE to welcome people as staling</h1>") 

def about_stalin(request):
    return HttpResponse("<h1>расстрелять</h1>")
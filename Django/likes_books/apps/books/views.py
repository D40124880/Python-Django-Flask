from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return render(request, "books/index.html")
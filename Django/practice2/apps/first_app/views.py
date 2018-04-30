from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from time import gmtime, strftime
from django.utils.crypto import get_random_string

from models import *

# Create your views here.

# def index(request):
#     #anything you did in the shell you can insert here
#     print strftime('%Y-%m-%d %H:%M:%S', gmtime())
#     print get_random_string(length=14)

#     return render(request, 'first_app/index.html', {"first_app": First_app.objects.all() })

#soooo here is where the functions go

# url(r'^create$', views.create)
def create(request):
    if request.method == "POST":
        print "*"*50
        print request.POST
        print request.POST['name']
        print request.POST['desc']
        request.session['name'] = "test"
        print "*"*50
        return redirect("/")
    else:
        return redirect("/")

        

def index(request):
    # response = "placeholder to later display all the lists of blogs"
    context = {
        "email":"blog@gmail.com",
        "name":"mike",
    }
    return render(request, "first_app/index.html", context)

def new(request):
    response = "placeholder to display a new form to create a new blog"
    return HttpResponse(response)

# def create(request):
#     return redirect('/')

def show(request, number1):
    return HttpResponse("This is number 1: " + number1)

def edit(request, number2):
    return HttpResponse("placeholder to edit blog: " + number2)

def destroy(request, number3):
    return redirect('/')
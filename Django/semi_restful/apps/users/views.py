from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from .models import *
from datetime import datetime
from time import strftime, gmtime

# Create your views here.
def index(request):
    context = {
        'users' : User.objects.all(),
    }
    return render(request, "users/index.html", context)

def new(request):
    #generate the form
    return render(request, "users/new.html")

def create(request):
    #handle form submission
    User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'])
    return redirect('/')

def show(request, user_id):
    context = {
        'user' : User.objects.get(id = user_id)
    }
    return render(request, "users/show.html", context)

def edit(request, user_id):
    context = {
        'user' : User.objects.get(id = user_id)
    }
    return render(request, "users/edit.html", context)

def update(request):
    user = User.objects.get(id = request.POST['user_id'])
    user.first_name = request.POST['first_name']
    user.last_name = request.POST['last_name']
    user.email = request.POST['email']
    user.save()
    return redirect('/')

def destroy(request, user_id):
    User.objects.get(id = user_id).delete()
    return redirect('/')
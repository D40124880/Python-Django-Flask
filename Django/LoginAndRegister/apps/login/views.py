from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import*
import bcrypt
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your views here.

def index(request):

    return render(request,"login/index.html")

def process(request):
    if request.method == "POST":
        error = False
        if len(request.POST['first_name']) < 2:
            messages.error(request, 'First Name must be longer than 2 characters')
            error = True
        if any(char.isdigit() for char in request.POST['first_name']):
            messages.error(request, 'First Name cannot contain letters')
            error = True
        if len(request.POST['last_name']) < 2:
            messages.error(request, 'Last Name must be longer than 2 characters')
            error = True
        if any(char.isdigit() for char in request.POST['last_name']):
            messages.error(request, 'Last Name cannot contain letters')
        if len(request.POST['password']) < 8:
            messages.error(request, 'Password must be at least 8 characters')
            error = True
        if not EMAIL_REGEX.match(request.POST['email']):
            messages.error(request, 'Invalid email address')
            error = True
        if request.POST['password'] != request.POST['confirm_pw']:
            messages.error(request, 'Password and Confirmation must match!')
            error = True
        if error:
            return redirect("/")
        
        hash1 = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        this_user = user.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'],
        email=request.POST['email'],password=hash1)
        request.session['id'] = this_user.id
        
        return redirect("/success")
    else:
        return redirect("/")
def login(request):
    if request.method == "POST":
        try:
            users = user.objects.get(email=request.POST['email'])
        except:
            messages.error(request, 'Invalid email')
            return redirect("/")
        if bcrypt.checkpw(request.POST['password'].encode(), users.password.encode()):
            request.session['id'] = users.id
            
            return redirect("/success")
    else:
        return redirect("/")
def success(request):
    context = {
        'users': user.objects.get(id=request.session['id'])
    }
    return render(request,"login/success.html", context)
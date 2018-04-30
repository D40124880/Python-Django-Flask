from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

#soooo here is where the functions go

def index(request):
    # response = "placeholder to later display all the lists of blogs"
    context = {
        "email":"blog@gmail.com",
        "name":"mike",
    }
    return render(request, "first_app/blah.html", context)

def new(request):
    response = "placeholder to display a new form to create a new blog"
    return HttpResponse(response)

def create(request):
    return redirect('/')

def show(request, number1):
    return HttpResponse("This is number 1: " + number1)

def edit(request, number2):
    return HttpResponse("placeholder to edit blog: " + number2)

def destroy(request, number3):
    return redirect('/')
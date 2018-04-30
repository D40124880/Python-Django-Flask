from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from time import gmtime, localtime, strftime
from django.utils.crypto import get_random_string


# Create your views here.

def index(request):
    context = {
        "date" : strftime("%b"" ""%d"","" %Y"),
        "time": strftime("%I:%M %p", gmtime()),
    }
    
    return render(request, "first_app/index.html", context)
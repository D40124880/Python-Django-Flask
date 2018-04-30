from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

# request.session.modified = True

# Create your views here.
def index(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0

    return render(request, "first_app/index.html")

def process(request):
    request.session['counter']+=1
    randomSTR = get_random_string(length = 14)
    request.session['random_word'] = randomSTR
    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')

# if request.method != "POST"
#     return redirect('/')
from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

# Create your views here.
def index(request):
    request.session['words'] = []
    return render(request, "words/index.html")

def addword(request):
    date = strftime("%H:%M:%S %p %B %dth, %Y", gmtime())
    msg = "- added on " + date
    alist = request.session['words']
    if 'bigfont' not in request.POST:
        fontclass = 'small'
    else:
        fontclass = 'big'
    invalues = {
        'newword' : request.POST['word'],
        'createDT' : msg,
        'color' : request.POST['color'],
        'bigfont' : fontclass
    }
    alist.append(invalues)
    request.session['words'] = alist
    return redirect('/show')

def show(request):
    return render(request, "words/index.html")

def clear(request):
    del request.session['words']
    request.session['words'] = []
    return render(request, "words/index.html")

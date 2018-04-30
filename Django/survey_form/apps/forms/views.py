from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    if "counter" not in request.session:
        request.session['counter'] = 0
    return render(request, "forms/index.html")

def process(request):
    request.session['counter']+=1
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']
    return redirect('/result')

def result(request):
    context = {
        "count" : request.session['counter'],
        "name" : request.session['name'],
        "location" : request.session['location'],
        "language" : request.session['language'],
        "comment" : request.session['comment'],
    }
    return render(request, "forms/result.html", context)
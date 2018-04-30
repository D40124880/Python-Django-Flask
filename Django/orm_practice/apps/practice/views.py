from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    context = {"authors": Author.objects.all()}
    return render(request, "practice/index.html", context)
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "compare/index.html")

def add_compare(request):
    return render(request, "compare/add_compare.html")
    


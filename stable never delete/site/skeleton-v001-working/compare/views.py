#from ast import Compare
from multiprocessing import context
from django.shortcuts import render
import json
from compare.models import Groceries


#from compare.models import .
# Create your views here.

def index(request):
    #this gets the item objects
    _items = Groceries.objects.all()
    #renders the page
    return render(request, "index.html", {"items": _items})
    

# def page_2(request):
#     #this get this objects stored in db in class Project
#     projects = Project.objects.all()
#     url = str(Project.image).replace("static", "")
#     context = {
#         "projects": projects, "url": url
#     }
#     return render(request, "page_2.html", context)

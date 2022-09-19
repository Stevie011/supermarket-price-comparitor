from django.shortcuts import render
from compare.models import Project, Work, Item
# Create your views here.

def index(request):
    #this gets the item objects
    _items = Item.objects.all()
    #renders the page and also gives it the item list
    # for i in _items:
    #     print(i)
    print(_items)
    print("hello")
    return render(request, "index.html", {"items": _items})
    #print(_items)



def page_2(request):
    #this get this objects stored in db in class Project
    projects = Project.objects.all()
    url = str(Project.image).replace("static", "")
    context = {
        "projects": projects, "url": url
    }
    return render(request, "page_2.html", context)

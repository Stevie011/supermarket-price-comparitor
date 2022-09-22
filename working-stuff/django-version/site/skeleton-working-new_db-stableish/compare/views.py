#from ast import Compare
from django.shortcuts import render

from compare.models import Groceries


#from compare.models import .
# Create your views here.

def index(request):
    #this gets the item objects
    _items = Groceries.objects.all()
    # _items=[]
    # for i in _objs:
    #     _items.append(i.itemname)

    # print(_items)
    # for i in _objs:
    #     print(i.itemname)

    #print(_items)
    #renders the page and also gives it the item list
    print("harzit")
    return render(request, "index.html", {"items": _items})
    
    #return render(request, "index.html")
    #print("***", _items)

# def page_2(request):
#     #this get this objects stored in db in class Project
#     projects = Project.objects.all()
#     url = str(Project.image).replace("static", "")
#     context = {
#         "projects": projects, "url": url
#     }
#     return render(request, "page_2.html", context)

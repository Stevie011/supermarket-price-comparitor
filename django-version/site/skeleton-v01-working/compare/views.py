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
    # item_list=[]
    # for i in _items:
    #     item_list.append(i.itemname)
    # #print(item_list)
    # item_list_json = json.dumps(_items)
    # context = {"json_list": item_list_json}

    # print(_items)
    # for i in _items:
    #     print(i.checkers_price)

    #print(_items)
    #renders the page and also gives it the item list
    #print("harzit")
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

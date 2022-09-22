from django.shortcuts import render
from compare.models import Project, Work
# Create your views here.

def index(request):
    return render(request, "index.html")

def page_2(request):
    #this get this objects stored in db in class Project
    projects = Project.objects.all()
    url = str(Project.image).replace("static", "")
    context = {
        "projects": projects, "url": url
    }
    return render(request, "page_2.html", context)
